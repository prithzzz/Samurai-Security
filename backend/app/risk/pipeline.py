from app.risk.report_generator import generate_report
from app.risk.risk_engine import check_consistency
from app.risk.approval_system import (requires_approval, create_approval_request)

def run_risk_pipeline(model_name: str, evaluation_results: dict) -> dict:
    """Final stage: converts evaluation into report"""

    responses = evaluation_results.get("responses", [])

    consistency = check_consistency(responses)
    evaluation_results["consistency"] = consistency

    report = generate_report(model_name, evaluation_results)

    # Approval check
    if requires_approval(report):
        approval = create_approval_request(report)

        report["approval_required"] = True
        report["approval"] = approval
    else:
        report["approval_required"] = False

    return report