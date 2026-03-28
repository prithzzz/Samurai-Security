import { useNavigate } from "react-router-dom";

export default function Navbar() {
  const navigate = useNavigate();

  return (
    <div className="navbar">
      <h2>Samurai Security</h2>

      <div>
        <button onClick={() => navigate("/")}>Dashboard</button>
        <button onClick={() => navigate("/scan")}>Scan</button>
        <button onClick={() => navigate("/report")}>Report</button>
        <button
          onClick={() => navigate("/heal")}
          style={{
            background: "linear-gradient(135deg, #5cc8ff, #38bdf8)",
            color: "#001219",
            fontWeight: "bold",
            border: "none",
            boxShadow: "0 0 10px rgba(92,200,255,0.35)",
          }}
        >
          ⚡ Guardian
        </button>
      </div>
    </div>
  );
}