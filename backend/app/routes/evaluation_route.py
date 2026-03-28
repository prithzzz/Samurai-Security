# from fastapi import APIRouter
# from app.evaluation.pipeline import run_evaluation_pipeline

# router = APIRouter(prefix="/evaluation", tags=["Evaluation"])


# @router.post("/run")
# def run_evaluation(core_output: dict):
#     """Runs only the evaluation layer"""
#     result = run_evaluation_pipeline(core_output)

#     return {
#         "message": "Evaluation completed",
#         "data": result
#     }
# app/routes/evaluation_route.py

from fastapi import APIRouter
from pydantic import BaseModel
from typing import List, Optional

from app.evaluation.pipeline import EvaluationPipeline

router = APIRouter()

# Initialize pipeline once
pipeline = EvaluationPipeline()


# 🔹 Request Schema
class AttackInput(BaseModel):
    id: int
    prompt: str
    response: str
    conversation: Optional[List[str]] = []


# 🔹 Route
@router.post("/evaluate")
def evaluate_attacks(attacks: List[AttackInput]):
    """
    Runs evaluation pipeline on given attack data
    """

    # Convert pydantic objects → dict
    attack_data = [attack.dict() for attack in attacks]

    # Run pipeline
    results = pipeline.evaluate(attack_data)

    return {
        "status": "success",
        "results": results
    }