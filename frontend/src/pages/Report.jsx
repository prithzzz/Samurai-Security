import { useLocation } from "react-router-dom";

export default function Report() {
  const location = useLocation();
  const prompt = location.state?.prompt || "No input provided";

  return (
    <div className="report-page fade-in">
      <h1 className="report-title">📊 Analysis Report</h1>

      <p style={{ opacity: 0.7, marginBottom: "20px" }}>
        Input: {prompt}
      </p>

      <div className="section">
        <h2>Risk Score</h2>
        <div className="card-container">
          <div className="card">
            <h3>Risk Score</h3>
            <p style={{ color: "red", fontSize: "22px" }}>75%</p>
          </div>
        </div>
      </div>

      <div className="section">
        <h2>Attacks</h2>
        <div className="card-container">
          <div className="card">Prompt Injection</div>
          <div className="card">Data Leakage</div>
        </div>
      </div>

      <div className="section">
        <h2>Recommendations</h2>
        <div className="card-container">
          <div className="card">Use Validation</div>
          <div className="card">Improve Dataset</div>
        </div>
      </div>
    </div>
  );
}