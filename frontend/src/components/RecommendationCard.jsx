const RecommendationCard = ({ rec }) => {
  return (
    <div className="card">
      <h3>Fix</h3>
      <p>{rec}</p>
    </div>
  );
};

export default RecommendationCard;