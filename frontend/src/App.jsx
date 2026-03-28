import { useState } from "react";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import Navbar from "./components/Navbar";
import Dashboard from "./pages/Dashboard";
import ScanPage from "./pages/ScanPage";
import Report from "./pages/Report";
import HealPage from "./pages/healPage";

function App() {
  const [scanData, setScanData] = useState(null);

  return (
    <BrowserRouter>
      <Navbar />

      <Routes>
        <Route path="/" element={<ScanPage setScanData={setScanData} />} />
        <Route path="/dashboard" element={<Dashboard scanData={scanData} />} />
        <Route path="/scan" element={<ScanPage setScanData={setScanData} />} />
        <Route path="/report" element={<Report scanData={scanData} />} />
        <Route path="/heal" element={<HealPage scanData={scanData} />} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;