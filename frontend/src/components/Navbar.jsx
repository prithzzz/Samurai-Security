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
      </div>
    </div>
  );
}