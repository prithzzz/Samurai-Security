from pydantic import BaseModel
from typing import List

class EvaluationSchema(BaseModel):
    leakage_score: float
    bias_flag: bool
    jailbreak_detected: bool
    memory_attack: bool
    responses: list[str]