import { useState } from "react";
import { scanModel } from "../services/api";

export const useScan = () => {
  const [loading, setLoading] = useState(false);

  const runScan = async (input) => {
    setLoading(true);
    const res = await scanModel(input);
    setLoading(false);
    return res;
  };

  return { runScan, loading };
};