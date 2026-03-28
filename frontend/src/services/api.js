const BASE_URL = "http://127.0.0.1:8000"; // ✅ updated port

export const analyzeModel = async (input) => {
  try {
    const res = await fetch(`${BASE_URL}/scan`, { // ✅ updated endpoint
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ input }), // ✅ keep same format
    });

    const data = await res.json();
    return data;

  } catch (err) {
    console.error("API Error:", err);
    return null;
  }
};
export const healModel = async ({ systemPrompt, riskReport, evaluation, threshold, selfHeal }) => {
  try {
    const res = await fetch(`${BASE_URL}/heal`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        system_prompt: systemPrompt,
        risk_report:   riskReport,
        evaluation:    evaluation,
        threshold:     threshold,
        self_heal:     selfHeal,
      }),
    });
    const data = await res.json();
    return data;
  } catch (err) {
    console.error("Heal API Error:", err);
    return null;
  }
};