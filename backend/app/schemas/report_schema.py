from pydantic import BaseModel
from typing import List, Dict, Any

class ConsistencySchema(BaseModel):
    consistent: bool
    variance: float
    risk: str

class ReportSchema(BaseModel):
    model: str
    risk_score: float
    risk_level: str
    risk_breakdown: Dict[str, str]
    identified_vulnerabilities: List[str]
    recommendations: List[str]
    consistency: ConsistencySchema