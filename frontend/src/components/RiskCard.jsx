const RiskCard = ({ risk }) => {
  return (
    <div className="card">
      <h3>Risk Score</h3>
      <h1 style={{ color: "red" }}>{risk}%</h1>
    </div>
  );
};

export default RiskCard;