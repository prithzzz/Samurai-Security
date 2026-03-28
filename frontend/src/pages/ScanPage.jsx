import { useNavigate } from "react-router-dom";
import { useState } from "react";
import { analyzeModel } from "../services/api"; // ✅ import API

export default function ScanPage() {
  const navigate = useNavigate();
  const [prompt, setPrompt] = useState("");

  const handleAnalyze = async () => {
    try {
      // ✅ call backend
      const result = await analyzeModel(prompt);

      console.log("Backend response:", result);

      if (!result) {
        alert("Failed to connect to the backend server.");
        return;
      }
      if (result.error) {
        alert("Scanner Error: " + result.error + (result.reason ? ` - ${result.reason}` : ""));
        return;
      }

      // ✅ send result to report page
      navigate("/report", { state: { result, prompt } });

    } catch (error) {
      console.error("Scan failed:", error);
    }
  };

  return (
    <div className="center-page">
      <h1 className="main-title">🛡 Scan Model</h1>

      <div className="glass-card fade-in">
        <h2>Enter Model / Prompt</h2>

        <textarea
          className="big-input"
          placeholder="Type your model prompt here..."
          value={prompt}
          onChange={(e) => setPrompt(e.target.value)}
        />

        <button className="analyze-btn" onClick={handleAnalyze}>
          Analyze
        </button>
      </div>
    </div>
  );
}