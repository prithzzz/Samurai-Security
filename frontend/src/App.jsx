import { BrowserRouter, Routes, Route } from "react-router-dom";
import Navbar from "./components/Navbar";
import Dashboard from "./pages/Dashboard";
import ScanPage from "./pages/ScanPage";
import Report from "./pages/Report";

function App() {
  return (
    <BrowserRouter>
      <Navbar />

      <Routes>
        <Route path="/" element={<Dashboard />} />
        <Route path="/scan" element={<ScanPage />} />
        <Route path="/report" element={<Report />} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;