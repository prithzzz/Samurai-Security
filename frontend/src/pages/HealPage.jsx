import { useState } from "react";
import { useLocation, useNavigate } from "react-router-dom";
import { healModel } from "../services/api";

// ── tiny helpers ────────────────────────────────────────────────────────────
const scoreColor = (s) =>
  s >= 8 ? "#ef4444" : s >= 5 ? "#f59e0b" : "#22c55e";

const statusMeta = {
  patched:   { icon: "🛡️", label: "Fully Patched",       bg: "rgba(34,197,94,0.12)",   border: "#22c55e" },
  partial:   { icon: "⚠️", label: "Partially Mitigated", bg: "rgba(245,158,11,0.12)",  border: "#f59e0b" },
  unchanged: { icon: "🔴", label: "Could Not Mitigate",  bg: "rgba(239,68,68,0.12)",   border: "#ef4444" },
  skipped:   { icon: "⏭️", label: "Healing Skipped",     bg: "rgba(92,200,255,0.08)",  border: "#5cc8ff" },
};

// ── pipeline step component ─────────────────────────────────────────────────
function PipeStep({ icon, label, state }) {
  const colors = {
    idle:    { border: "#1e3a50", bg: "rgba(20,40,60,0.4)",  glow: "none" },
    active:  { border: "#5cc8ff", bg: "rgba(92,200,255,0.12)", glow: "0 0 14px rgba(92,200,255,0.35)" },
    done:    { border: "#22c55e", bg: "rgba(34,197,94,0.1)",  glow: "none" },
    skipped: { border: "#334155", bg: "rgba(20,40,60,0.2)",   glow: "none" },
  };
  const c = colors[state] || colors.idle;
  return (
    <div style={{ display:"flex", flexDirection:"column", alignItems:"center", gap:6, opacity: state==="skipped" ? 0.35 : 1, transition:"opacity 0.4s" }}>
      <div style={{
        width:46, height:46, borderRadius:10,
        border:`1px solid ${c.border}`, background:c.bg,
        boxShadow:c.glow, display:"flex", alignItems:"center", justifyContent:"center",
        fontSize:20, transition:"all 0.4s",
      }}>{state==="active" ? <span className="spin-icon">⚙️</span> : icon}</div>
      <span style={{ fontSize:"0.6rem", color:"#94a3b8", letterSpacing:"0.04em", textAlign:"center", maxWidth:70 }}>{label}</span>
    </div>
  );
}

function Arrow({ active }) {
  return (
    <div style={{
      flex:"0 0 28px", height:1,
      background: active ? "linear-gradient(90deg,#5cc8ff,#22c55e)" : "#1e3a50",
      transition:"background 0.5s", position:"relative",
    }}>
      <span style={{ position:"absolute", right:-2, top:-7, fontSize:8, color: active ? "#22c55e" : "#1e3a50" }}>▶</span>
    </div>
  );
}

export default function HealPage() {
  const location = useLocation();
  const navigate  = useNavigate();

  // Pre-populate from scan result if navigated from Report page
  const prefill = location.state || {};

  const [systemPrompt, setSystemPrompt] = useState(prefill.systemPrompt || "");
  const [threshold,    setThreshold]    = useState(5);
  const [selfHeal,     setSelfHeal]     = useState(true);
  const [loading,      setLoading]      = useState(false);
  const [result,       setResult]       = useState(null);
  const [log,          setLog]          = useState([]);
  const [pipeState,    setPipeState]    = useState({
    input:"idle", scan:"idle", eval:"idle", heal:"idle", verify:"idle", output:"idle"
  });

  const addLog = (msg, type="info") =>
    setLog(prev => [...prev, { msg, type, ts: Date.now() }]);

  const setPipe = (updates) =>
    setPipeState(prev => ({ ...prev, ...updates }));

  const handleHeal = async () => {
    if (!systemPrompt.trim() && !prefill.riskReport) {
      alert("Paste a system prompt or run a scan first.");
      return;
    }

    setLoading(true);
    setResult(null);
    setLog([]);
    setPipeState({ input:"idle", scan:"idle", eval:"idle", heal:"idle", verify:"idle", output:"idle" });

    // animate pipeline stages
    const delay = (ms) => new Promise(r => setTimeout(r, ms));

    setPipe({ input:"active" }); addLog("Receiving prompt + scan report…", "info"); await delay(450);
    setPipe({ input:"done", scan:"active" }); addLog("Analysing identified vulnerabilities…", "info"); await delay(550);
    setPipe({ scan:"done", eval:"active" }); addLog(`Initial risk score: ${prefill.riskReport?.risk_score ?? "—"}`, "warn"); await delay(500);
    setPipe({ eval:"done", heal: selfHeal ? "active" : "skipped" });

    if (selfHeal) {
      addLog("Self-Healing loop initiated…", "info"); await delay(400);
    } else {
      addLog("Self-Healing is OFF — returning report only.", "warn");
    }

    const payload = {
        systemPrompt,
        riskReport: prefill.riskReport || {},
        evaluation: prefill.evaluation || {},
        threshold,
        selfHeal,
    };
    console.log("HEAL PAYLOAD:", payload);
    const data = await healModel(payload);

    if (!data) {
      addLog("Heal API returned no response.", "error");
      setPipe({ heal:"done", verify:"skipped", output:"done" });
      setLoading(false);
      return;
    }

    // Log patch iterations
    if (selfHeal && data.patch_log) {
      for (const iter of data.patch_log) {
        addLog(`Iteration ${iter.iteration}: ${iter.patches_applied?.length ?? 0} patch(es) applied → score ${iter.score_after}`, "success");
        await delay(350);
      }
    }

    setPipe({ heal:"done", verify: selfHeal ? "active" : "skipped" }); await delay(400);
    addLog(`Final risk score: ${data.final_risk_score ?? data.risk_report?.risk_score ?? "—"}`, data.status === "patched" ? "success" : "warn");
    setPipe({ verify:"done", output:"active" }); await delay(300);
    setPipe({ output:"done" });

    setResult(data);
    setLoading(false);
  };

  const meta = result ? (statusMeta[result.status] || statusMeta.skipped) : null;
  const pipeActive = loading || !!result;

  return (
    <div style={{ minHeight:"100vh", padding:"30px 20px", maxWidth:1100, margin:"0 auto" }}>

      {/* Header */}
      <div style={{ display:"flex", alignItems:"center", gap:14, marginBottom:28 }}>
        <button onClick={() => navigate(-1)} style={{
          background:"rgba(92,200,255,0.1)", border:"1px solid #5cc8ff",
          color:"#5cc8ff", padding:"6px 14px", borderRadius:8, cursor:"pointer", fontSize:"0.8rem"
        }}>← Back</button>
        <div>
          <h1 style={{ margin:0, fontSize:"1.8rem", color:"#5cc8ff" }}>Self-Healing Guardian</h1>
          <p style={{ margin:0, fontSize:"0.75rem", color:"#64748b" }}>
            Iterative Prompt Hardening · Defensive Design Patterns · Zero-Touch Patching
          </p>
        </div>
        <div style={{ marginLeft:"auto", display:"flex", alignItems:"center", gap:6,
          background:"rgba(34,197,94,0.08)", border:"1px solid rgba(34,197,94,0.3)",
          borderRadius:100, padding:"5px 14px", fontSize:"0.68rem", color:"#22c55e" }}>
          <span style={{ width:7, height:7, borderRadius:"50%", background:"#22c55e",
            display:"inline-block", animation:"pulse 2s infinite" }}></span>
          GUARDIAN ACTIVE
        </div>
      </div>

      <div style={{ display:"grid", gridTemplateColumns:"1fr 1fr", gap:20 }}>

        {/* ── LEFT: config ── */}
        <div style={{ display:"flex", flexDirection:"column", gap:16 }}>

          {/* Self-Heal Toggle */}
          <div style={{
            background:"rgba(20,40,60,0.7)", border:"1px solid #1e3a50",
            borderRadius:14, padding:"18px 20px",
            display:"flex", alignItems:"center", justifyContent:"space-between"
          }}>
            <div>
              <div style={{ fontWeight:700, fontSize:"0.95rem", marginBottom:2 }}>Self-Healing Mode</div>
              <div style={{ fontSize:"0.7rem", color:"#64748b" }}>
                Auto-patch vulnerabilities and re-validate in a feedback loop
              </div>
            </div>
            <div
              onClick={() => setSelfHeal(p => !p)}
              style={{
                width:50, height:26, borderRadius:13, cursor:"pointer",
                background: selfHeal ? "#5cc8ff" : "#1e3a50",
                position:"relative", transition:"background 0.3s", flexShrink:0, marginLeft:16,
              }}
            >
              <div style={{
                position:"absolute", top:3,
                left: selfHeal ? 26 : 3,
                width:20, height:20, borderRadius:"50%", background:"#fff",
                transition:"left 0.3s",
              }}/>
            </div>
          </div>

          {/* System Prompt */}
          <div style={{ background:"rgba(20,40,60,0.7)", border:"1px solid #1e3a50", borderRadius:14, padding:20 }}>
            <label style={{ display:"block", fontSize:"0.68rem", color:"#64748b",
              letterSpacing:"0.07em", textTransform:"uppercase", marginBottom:8 }}>
              System Prompt to Harden
            </label>
            <textarea
              value={systemPrompt}
              onChange={e => setSystemPrompt(e.target.value)}
              rows={6}
              placeholder="Paste the system instructions you want the Guardian to harden…"
              style={{
                width:"100%", background:"#0b1c2c", border:"1px solid #1e3a50",
                borderRadius:8, color:"#e6f1ff", fontFamily:"'Segoe UI', monospace",
                fontSize:"0.78rem", padding:12, resize:"vertical", outline:"none",
                boxSizing:"border-box",
              }}
            />
          </div>

          {/* Threshold */}
          <div style={{ background:"rgba(20,40,60,0.7)", border:"1px solid #1e3a50", borderRadius:14, padding:20 }}>
            <label style={{ display:"block", fontSize:"0.68rem", color:"#64748b",
              letterSpacing:"0.07em", textTransform:"uppercase", marginBottom:8 }}>
              Risk Threshold — <span style={{ color:"#5cc8ff" }}>{threshold}</span>
            </label>
            <input type="range" min={1} max={9} step={0.5} value={threshold}
              onChange={e => setThreshold(parseFloat(e.target.value))}
              style={{ width:"100%", accentColor:"#5cc8ff" }}
            />
            <div style={{ fontSize:"0.62rem", color:"#475569", marginTop:6 }}>
              Healing triggers when risk score exceeds this value (scale 0–10)
            </div>
          </div>

          {/* Run button */}
          <button onClick={handleHeal} disabled={loading} style={{
            padding:"14px", borderRadius:12, border:"none",
            background: loading ? "#1e3a50" : "linear-gradient(135deg,#5cc8ff,#38bdf8)",
            color: loading ? "#64748b" : "#001219",
            fontWeight:700, fontSize:"0.95rem", cursor: loading ? "not-allowed" : "pointer",
            transition:"all 0.2s", letterSpacing:"0.04em",
          }}>
            {loading ? "Healing in progress…" : "Activate Guardian"}
          </button>

          {/* Healing log */}
          {log.length > 0 && (
            <div style={{
              background:"#050e15", border:"1px solid #1e3a50", borderRadius:10,
              padding:14, fontFamily:"monospace", fontSize:"0.72rem", maxHeight:200,
              overflowY:"auto", lineHeight:1.9,
            }}>
              {log.map((l, i) => (
                <div key={i} style={{
                  color: l.type==="success" ? "#22c55e" : l.type==="warn" ? "#f59e0b"
                       : l.type==="error" ? "#ef4444" : "#5cc8ff"
                }}>
                  [{new Date(l.ts).toISOString().substr(17,6)}] {l.msg}
                </div>
              ))}
            </div>
          )}
        </div>

        {/* ── RIGHT: output ── */}
        <div style={{ display:"flex", flexDirection:"column", gap:16 }}>

          {/* Pipeline visualiser */}
          <div style={{ background:"rgba(20,40,60,0.7)", border:"1px solid #1e3a50", borderRadius:14, padding:20 }}>
            <div style={{ fontSize:"0.68rem", color:"#64748b", letterSpacing:"0.07em",
              textTransform:"uppercase", marginBottom:14 }}>Pipeline Flow</div>
            <div style={{ display:"flex", alignItems:"center", gap:0, overflowX:"auto" }}>
              <PipeStep icon="📥" label="Input"    state={pipeState.input}  />
              <Arrow active={pipeState.scan !== "idle"} />
              <PipeStep icon="🔬" label="Scan"     state={pipeState.scan}   />
              <Arrow active={pipeState.eval !== "idle"} />
              <PipeStep icon="⚖️" label="Evaluate" state={pipeState.eval}   />
              <Arrow active={pipeState.heal !== "idle"} />
              <PipeStep icon="🩹" label="Heal"     state={pipeState.heal}   />
              <Arrow active={pipeState.verify !== "idle"} />
              <PipeStep icon="✅" label="Verify"   state={pipeState.verify} />
              <Arrow active={pipeState.output !== "idle"} />
              <PipeStep icon="📤" label="Output"   state={pipeState.output} />
            </div>
          </div>

          {/* Results */}
          {!result && !loading && (
            <div style={{
              background:"rgba(20,40,60,0.4)", border:"1px dashed #1e3a50",
              borderRadius:14, padding:40, textAlign:"center", color:"#334155"
            }}>
              <div style={{ fontSize:36, marginBottom:12 }}>🛡️</div>
              <div style={{ fontSize:"0.8rem" }}>
                Activate the Guardian to see the hardened prompt & risk delta
              </div>
            </div>
          )}

          {result && (
            <>
              {/* Status badge */}
              <div style={{
                background: meta.bg, border:`1px solid ${meta.border}`,
                borderRadius:14, padding:"16px 20px",
                display:"flex", alignItems:"center", gap:14,
              }}>
                <span style={{ fontSize:28 }}>{meta.icon}</span>
                <div>
                  <div style={{ fontWeight:700, fontSize:"1rem", color: meta.border }}>{meta.label}</div>
                  <div style={{ fontSize:"0.72rem", color:"#94a3b8" }}>
                    {result.iterations} iteration{result.iterations !== 1 ? "s" : ""} ·{" "}
                    {result.improvement_pct}% risk reduction
                  </div>
                </div>
              </div>

              {/* Score comparison */}
              <div style={{ display:"grid", gridTemplateColumns:"1fr 1fr", gap:12 }}>
                {[
                  { label:"Initial Risk", val: result.initial_risk_score, sub:"before healing" },
                  { label:"Final Risk",   val: result.final_risk_score,   sub:"after healing"  },
                ].map(({ label, val, sub }) => (
                  <div key={label} style={{
                    background:"rgba(20,40,60,0.7)", border:"1px solid #1e3a50",
                    borderRadius:12, padding:16,
                  }}>
                    <div style={{ fontSize:"0.62rem", color:"#64748b", letterSpacing:"0.07em",
                      textTransform:"uppercase", marginBottom:6 }}>{label}</div>
                    <div style={{ fontSize:"2rem", fontWeight:700, color: scoreColor(val), lineHeight:1 }}>
                      {val?.toFixed(1) ?? "—"}
                    </div>
                    <div style={{ fontSize:"0.62rem", color:"#475569", marginTop:4 }}>{sub}</div>
                  </div>
                ))}
              </div>

              {/* Diff view */}
              {result.status !== "skipped" && (
                <div style={{ display:"grid", gridTemplateColumns:"1fr 1fr", gap:12 }}>
                  {[
                    { label:"Before — Vulnerable", content: result.original_prompt, hdr:"rgba(239,68,68,0.08)", bdr:"rgba(239,68,68,0.3)", clr:"#ef4444" },
                    { label:"After — Hardened",    content: result.hardened_prompt,  hdr:"rgba(34,197,94,0.08)",  bdr:"rgba(34,197,94,0.3)",  clr:"#22c55e" },
                  ].map(({ label, content, hdr, bdr, clr }) => (
                    <div key={label} style={{ background:"#050e15", border:`1px solid ${bdr}`, borderRadius:10, overflow:"hidden" }}>
                      <div style={{ background:hdr, padding:"8px 14px", fontSize:"0.62rem",
                        color:clr, letterSpacing:"0.06em", borderBottom:`1px solid ${bdr}` }}>
                        {label}
                      </div>
                      <pre style={{
                        margin:0, padding:"12px 14px", fontSize:"0.68rem",
                        color:"#e6f1ff", whiteSpace:"pre-wrap", wordBreak:"break-word",
                        maxHeight:160, overflowY:"auto", lineHeight:1.6,
                      }}>
                        {content || "(empty)"}
                      </pre>
                    </div>
                  ))}
                </div>
              )}



              {/* Final vulnerabilities */}
              {result.final_report?.identified_vulnerabilities?.length > 0 && (
                <div style={{ background:"rgba(20,40,60,0.7)", border:"1px solid #1e3a50", borderRadius:14, padding:20 }}>
                  <div style={{ fontSize:"0.68rem", color:"#64748b", letterSpacing:"0.07em",
                    textTransform:"uppercase", marginBottom:10 }}>Remaining Vulnerabilities</div>
                  <div style={{ display:"flex", flexWrap:"wrap", gap:8 }}>
                    {result.final_report.identified_vulnerabilities.map((v, i) => (
                      <span key={i} style={{
                        padding:"4px 12px", borderRadius:100, fontSize:"0.68rem",
                        background:"rgba(239,68,68,0.1)", border:"1px solid rgba(239,68,68,0.4)",
                        color:"#ef4444",
                      }}>{v.name || v}</span>
                    ))}
                  </div>
                </div>
              )}
            </>
          )}
        </div>
      </div>

      <style>{`
        @keyframes pulse { 0%,100%{opacity:1} 50%{opacity:0.3} }
        .spin-icon { display:inline-block; animation:spin 1s linear infinite; }
        @keyframes spin { to { transform:rotate(360deg) } }
      `}</style>
    </div>
  );
}