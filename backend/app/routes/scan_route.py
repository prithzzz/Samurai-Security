from fastapi import APIRouter
from app.core.pipeline import run_core

router = APIRouter()

"""core pipeline"""
@router.post("/scan")
def scan_model(input_data: dict):
    result = run_core(input_data)
    return result