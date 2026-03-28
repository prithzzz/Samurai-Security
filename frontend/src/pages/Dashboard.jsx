import { useNavigate } from "react-router-dom";

export default function Dashboard({ scanData }) {
  const navigate = useNavigate();

  if (!scanData) {
    return (
      <div className="main-content" style={{ textAlign: "center", paddingTop: 80 }}>
        <h2>No Data Available</h2>
        <p style={{ color: "gray" }}>Run a new scan to populate the dashboard.</p>
        <button className="analyze-btn" onClick={() => navigate("/")} style={{ marginTop: 20 }}>Start Scan</button>
      </div>
    );
  }

  const result = scanData.result || {};
  const risk = result.risk_analysis || {};
  const score = risk.risk_score ?? 0;
  const metrics = risk.risk_breakdown || {};

  return (
    <div className="main-content">
      <h1 className="main-title">📊 Dashboard Overview</h1>

      <div className="card-container">
        <div className="card fade-in">
          <h3>Risk Score</h3>
          <p style={{ color: score >= 8 ? "#ef4444" : score >= 5 ? "#f59e0b" : "#22c55e", fontSize: "24px", fontWeight: "bold" }}>
            {score} / 10
          </p>
        </div>

        <div className="card fade-in">
          <h3>Prompt Injection</h3>
          <p style={{ color: metrics["Jailbreak Vulnerability"] === "HIGH" ? "#ef4444" : "#22c55e", fontWeight: "bold" }}>
            {metrics["Jailbreak Vulnerability"] || "UNDETECTED"}
          </p>
        </div>

        <div className="card fade-in">
          <h3>Data Leakage</h3>
          <p style={{ color: metrics["Data Leakage"] === "HIGH" || metrics["Data Leakage"] === "MEDIUM" ? "#f59e0b" : "#22c55e", fontWeight: "bold" }}>
            {metrics["Data Leakage"] || "UNDETECTED"}
          </p>
        </div>

        <div className="card fade-in">
          <h3>Bias</h3>
          <p style={{ color: metrics["Bias Risk"] === "HIGH" ? "#ef4444" : "#22c55e", fontWeight: "bold" }}>
            {metrics["Bias Risk"] || "UNDETECTED"}
          </p>
        </div>
      </div>
    </div>
  );
}