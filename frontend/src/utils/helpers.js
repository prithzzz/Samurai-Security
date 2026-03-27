export const formatRisk = (risk) => {
  if (risk > 70) return "High";
  if (risk > 40) return "Medium";
  return "Low";
};