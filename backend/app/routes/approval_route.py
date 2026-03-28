from fastapi import APIRouter, HTTPException
from app.risk.approval_system import (
    get_approval_status,
    approve_request,
    reject_request
)

router = APIRouter(prefix="/approval", tags=["Approval"])


@router.get("/{approval_id}")
def get_status(approval_id: str):
    result = get_approval_status(approval_id)

    if "error" in result:
        raise HTTPException(status_code=404, detail=result["error"])

    return result


@router.post("/{approval_id}/approve")
def approve(approval_id: str, reviewer: str = "security_admin"):
    result = approve_request(approval_id, reviewer)

    if "error" in result:
        raise HTTPException(status_code=404, detail=result["error"])

    return {
        "message": "Approval granted",
        "data": result
    }


@router.post("/{approval_id}/reject")
def reject(
    approval_id: str,
    reviewer: str = "security_admin",
    reason: str = "Unsafe model behavior detected"
):
    result = reject_request(approval_id, reviewer, reason)

    if "error" in result:
        raise HTTPException(status_code=404, detail=result["error"])

    return {
        "message": "Approval rejected",
        "data": result
    }