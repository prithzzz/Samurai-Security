from fastapi import APIRouter, HTTPException
from app.healing.healing_engine import run_healing_pipeline

router = APIRouter()


@router.post("/heal")
def heal(data: dict):
    system_prompt = data.get("system_prompt")
    risk_report = data.get("risk_report")

    if not system_prompt or not risk_report:
        raise HTTPException(
            status_code=400,
            detail="system_prompt and risk_report are required"
        )

    result = run_healing_pipeline(
        system_prompt=system_prompt,
        initial_risk_report=risk_report,
        raw_evaluation=data.get("evaluation", {}),
        threshold=data.get("threshold"),
    )

    return result