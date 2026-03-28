import { useLocation, useNavigate } from "react-router-dom";

const scoreColor = (s) =>
  s >= 8 ? "#ef4444" : s >= 5 ? "#f59e0b" : "#22c55e";

export default function Report() {
  const location = useLocation();
  const navigate  = useNavigate();

  const result     = location.state?.result || {};
  const risk       = result.risk_analysis   || {};
  const evaluation = result.evaluation      || {};
  const summary    = result.summary         || {};
  const systemPrompt = result.system_prompt || location.state?.prompt || "";

  const score      = risk.risk_score  ?? "—";
  const level      = risk.risk_level  ?? "—";
  const vulns      = risk.identified_vulnerabilities || [];
  const recs       = risk.recommendations || [];
  const breakdown  = risk.risk_breakdown  || {};

  const handleHeal = () => {
    navigate("/heal", {
      state: {
        systemPrompt,
        riskReport:  risk,
        evaluation,
      },
    });
  };

  return (
    <div className="report-page fade-in">
      <h1 className="report-title">📊 Analysis Report</h1>

      {/* Risk Score */}
      <div className="section">
        <h2>Risk Score</h2>
        <div className="card-container">
          <div className="card">
            <h3>Risk Score</h3>
            <p style={{ color: scoreColor(score), fontSize: "2rem", fontWeight: 700 }}>
              {score}
              <span style={{ fontSize: "1rem", opacity: 0.6 }}> / 10</span>
            </p>
            <p style={{ opacity: 0.7 }}>Level: {level}</p>
          </div>
          <div className="card">
            <h3>Attack Summary</h3>
            <p>Total: {summary.total ?? "—"}</p>
            <p style={{ color: "#ef4444" }}>Risky: {summary.risky ?? "—"}</p>
            <p style={{ color: "#22c55e" }}>Safe:  {summary.safe  ?? "—"}</p>
          </div>
        </div>
      </div>

      {/* Risk Breakdown */}
      {Object.keys(breakdown).length > 0 && (
        <div className="section">
          <h2>Risk Breakdown</h2>
          <div className="card-container">
            {Object.entries(breakdown).map(([key, val]) => (
              <div className="card" key={key}>
                <h3 style={{ fontSize: "0.85rem" }}>{key}</h3>
                <p style={{ color: val === "HIGH" ? "#ef4444" : "#22c55e", fontWeight: 700 }}>
                  {val}
                </p>
              </div>
            ))}
          </div>
        </div>
      )}

      {/* Vulnerabilities */}
      {vulns.length > 0 && (
        <div className="section">
          <h2>Identified Vulnerabilities</h2>
          <div className="card-container">
            {vulns.map((v, i) => (
              <div className="card" key={i}>
                <h3 style={{ fontSize: "0.85rem" }}>{v.name || v}</h3>
                {v.severity && (
                  <p style={{ color: v.severity === "HIGH" ? "#ef4444" : "#f59e0b", fontSize: "0.8rem" }}>
                    {v.severity}
                  </p>
                )}
              </div>
            ))}
          </div>
        </div>
      )}

      {/* Recommendations */}
      {recs.length > 0 && (
        <div className="section">
          <h2>Recommendations</h2>
          <div className="card-container">
            {recs.map((r, i) => (
              <div className="card" key={i} style={{ fontSize: "0.82rem", textAlign: "left" }}>
                {r}
              </div>
            ))}
          </div>
        </div>
      )}

      {/* Guardian CTA */}
      <div className="section" style={{ textAlign: "center" }}>
        <button
          onClick={handleHeal}
          style={{
            padding: "14px 36px",
            borderRadius: 14,
            border: "none",
            background: "linear-gradient(135deg, #5cc8ff, #38bdf8)",
            color: "#001219",
            fontWeight: "bold",
            fontSize: "1rem",
            cursor: "pointer",
            boxShadow: "0 0 20px rgba(92,200,255,0.4)",
            transition: "0.3s",
          }}
        >
          ⚡ Activate Self-Healing Guardian
        </button>
        <p style={{ opacity: 0.5, fontSize: "0.75rem", marginTop: 8 }}>
          Auto-patch vulnerabilities and generate a hardened system prompt
        </p>
      </div>
    </div>
  );
}