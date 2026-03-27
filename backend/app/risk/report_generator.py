from app.risk.risk_engine import calculate_risk_score, categorize_risk, get_risk_breakdown
from app.risk.owasp_mapper import map_to_owasp
from app.risk.recommendation_engine import generate_recommendations

def generate_report(model_name: str, evaluation: dict) -> dict:
    score = calculate_risk_score(evaluation)
    level = categorize_risk(score)
    breakdown = get_risk_breakdown(evaluation)
    owasp_issues = map_to_owasp(evaluation)

    report = {
        "model": model_name,
        "risk_score": score,
        "risk_level": level,
        "risk_breakdown": breakdown,
        "identified_vulnerabilities": owasp_issues,
        "recommendations": generate_recommendations(owasp_issues),
        "consistency": evaluation.get("consistency", {}),
    }

    return report