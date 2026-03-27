import React, { useState } from "react";

const RiskDashboard = ({ data, onBack }) => {
  const [tab, setTab] = useState("overview");

  if (!data) return null;

  return (
    <div className="card dashboard">

      {/* 🔙 BACK BUTTON */}
      <button className="button back-btn" onClick={onBack}>
        ← Back
      </button>

      <h2>Risk Dashboard</h2>

      {/* Tabs */}
      <div className="tabs">
        <button className="button" onClick={() => setTab("overview")}>
          Overview
        </button>
        <button className="button" onClick={() => setTab("attacks")}>
          Attacks
        </button>
        <button className="button" onClick={() => setTab("risk")}>
          Risk
        </button>
        <button className="button" onClick={() => setTab("fixes")}>
          Fixes
        </button>
      </div>

      {/* CONTENT */}
      {tab === "overview" && (
        <h1 className="score">{data.risk_score}%</h1>
      )}

      {tab === "attacks" && (
        <div className="section">
          <p><b>Prompt Injection:</b> {data.prompt_injection}</p>
          <p><b>Adversarial:</b> {data.adversarial}</p>
        </div>
      )}

      {tab === "risk" && (
        <div className="section">
          <p><b>Data Leakage:</b> {data.data_leakage}</p>
          <p><b>Bias:</b> {data.bias}</p>
        </div>
      )}

      {tab === "fixes" && (
        <div className="section">
          <p>Use input validation</p>
          <p>Improve training data</p>
        </div>
      )}
    </div>
  );
};

export default RiskDashboard;