from fastapi import APIRouter
from app.schemas.evaluation_schema import EvaluationSchema
from app.risk.pipeline import run_risk_pipeline

router = APIRouter()

@router.post("/generate-report")
def generate_report_api(data: EvaluationSchema):
    result = run_risk_pipeline("TestModel", data.dict())
    return result