from app.risk.report_generator import generate_report
from app.risk.risk_engine import check_consistency

def run_risk_pipeline(model_name: str, evaluation_results: dict) -> dict:
    """Final stage: converts evaluation into report"""

    responses = evaluation_results.get("responses", [])

    consistency = check_consistency(responses)

    # Add it into evaluation
    evaluation_results["consistency"] = consistency

    report = generate_report(model_name, evaluation_results)

    return report