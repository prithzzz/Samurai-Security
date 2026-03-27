const BASE_URL = "http://localhost:5000";

export const analyzeModel = async (input) => {
  try {
    const res = await fetch(`${BASE_URL}/analyze`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ input }),
    });

    return await res.json();
  } catch (err) {
    console.error(err);
    return null;
  }
};