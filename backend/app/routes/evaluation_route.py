from fastapi import APIRouter
from app.evaluation.pipeline import run_evaluation_pipeline

router = APIRouter(prefix="/evaluation", tags=["Evaluation"])


@router.post("/run")
def run_evaluation(core_output: dict):
    """Runs only the evaluation layer"""
    result = run_evaluation_pipeline(core_output)

    return {
        "message": "Evaluation completed",
        "data": result
    }