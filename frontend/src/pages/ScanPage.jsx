import { useNavigate } from "react-router-dom";
import { useState } from "react";

export default function ScanPage() {
  const navigate = useNavigate();
  const [prompt, setPrompt] = useState("");

  const handleAnalyze = () => {
    navigate("/report", { state: { prompt } });
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