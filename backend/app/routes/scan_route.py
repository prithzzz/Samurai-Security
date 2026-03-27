from fastapi import APIRouter
from app.core.pipeline import run_core

router = APIRouter()

@router.post("/scan")
def scan_model(input_data: dict):
    """
    Runs core pipeline (Person B)
    """
    result = run_core(input_data)
    return result