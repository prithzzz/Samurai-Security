import { createContext, useState } from "react";

export const ScanContext = createContext();

export const ScanProvider = ({ children }) => {
  const [report, setReport] = useState(null);

  return (
    <ScanContext.Provider value={{ report, setReport }}>
      {children}
    </ScanContext.Provider>
  );
};