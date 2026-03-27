export default function Dashboard() {
  return (
    <div className="main-content">
      <h1 className="main-title">📊 Dashboard Overview</h1>

      <div className="card-container">
        <div className="card fade-in">
          <h3>Risk Score</h3>
          <p style={{ color: "red", fontSize: "24px" }}>75%</p>
        </div>

        <div className="card fade-in">
          <h3>Prompt Injection</h3>
          <p>Vulnerable</p>
        </div>

        <div className="card fade-in">
          <h3>Data Leakage</h3>
          <p>Detected</p>
        </div>

        <div className="card fade-in">
          <h3>Bias</h3>
          <p>Medium</p>
        </div>
      </div>
    </div>
  );
}