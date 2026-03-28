import { BrowserRouter, Routes, Route } from "react-router-dom";
import Navbar from "./components/Navbar";
import Dashboard from "./pages/Dashboard";
import ScanPage from "./pages/ScanPage";
import Report from "./pages/Report";
import HealPage from "./pages/healPage";

function App() {
  return (
    <BrowserRouter>
      <Navbar />

      <Routes>
        <Route path="/" element={<ScanPage />} />
        <Route path="/dashboard" element={<Dashboard />} />
        <Route path="/scan" element={<ScanPage />} />
        <Route path="/report" element={<Report />} />
        <Route path="/heal" element={<HealPage />} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;