import React from "react";

const getColor = (value) => {
  if (value.includes("Safe")) return "green";
  if (value.includes("Medium")) return "orange";
  return "red";
};

const AttackResults = ({ results }) => {
  if (!results) return null;

  return (
    <div className="card">
      <h2>Attack Results</h2>

      {Object.entries(results).map(([key, value]) => {
        if (key === "risk_score") return null;

        return (
          <div key={key} className="result-item">
            <p>
              <b>{key}</b>: {value}
            </p>

            <div className="progress-bar">
              <div className={`progress ${getColor(value)}`}></div>
            </div>
          </div>
        );
      })}
    </div>
  );
};

export default AttackResults;