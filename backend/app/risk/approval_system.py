import uuid
from datetime import datetime

"""for high risk processes"""

# In-memory storage (can later move to DB)
APPROVAL_STORE = {}

def requires_approval(report: dict) -> bool:
    if report.get("risk_level") == "HIGH":
        return True

    # Also trigger if critical vulnerabilities exist
    critical_issues = [
        "Prompt Injection Vulnerability",
        "Data Exfiltration Risk",
        "Sensitive Information Disclosure"
    ]

    detected = [issue["name"] for issue in report.get("identified_vulnerabilities", [])]

    return any(issue in detected for issue in critical_issues)


def create_approval_request(report: dict) -> dict:
    """Creates a human approval request for high-risk cases"""

    approval_id = str(uuid.uuid4())

    approval_request = {
        "approval_id": approval_id,
        "status": "PENDING",
        "created_at": datetime.utcnow().isoformat(),
        "risk_level": report.get("risk_level"),
        "risk_score": report.get("risk_score"),
        "summary": generate_summary(report),
        "report_summary": {
            "model": report.get("model"),
            "risk_score": report.get("risk_score"),
            "risk_level": report.get("risk_level"),
            "top_vulnerabilities": [
                v.get("name") for v in report.get("identified_vulnerabilities", [])[:3]
            ]
        }
    }

    APPROVAL_STORE[approval_id] = approval_request

    return approval_request


def generate_summary(report: dict) -> str:
    """Creates a short human-readable summary"""

    issues = report.get("identified_vulnerabilities", [])
    names = [i["name"] for i in issues]

    return (
        f"High-risk model behavior detected. "
        f"Risk Score: {report.get('risk_score')}. "
        f"Issues: {', '.join(names[:3])}"
    )


def get_approval_status(approval_id: str) -> dict:
    return APPROVAL_STORE.get(approval_id, {"error": "Not found"})


def approve_request(approval_id: str, reviewer: str) -> dict:
    if approval_id not in APPROVAL_STORE:
        return {"error": "Invalid approval ID"}

    APPROVAL_STORE[approval_id]["status"] = "APPROVED"
    APPROVAL_STORE[approval_id]["reviewed_by"] = reviewer
    APPROVAL_STORE[approval_id]["reviewed_at"] = datetime.utcnow().isoformat()

    return APPROVAL_STORE[approval_id]


def reject_request(approval_id: str, reviewer: str, reason: str) -> dict:
    if approval_id not in APPROVAL_STORE:
        return {"error": "Invalid approval ID"}

    APPROVAL_STORE[approval_id]["status"] = "REJECTED"
    APPROVAL_STORE[approval_id]["reviewed_by"] = reviewer
    APPROVAL_STORE[approval_id]["reason"] = reason
    APPROVAL_STORE[approval_id]["reviewed_at"] = datetime.utcnow().isoformat()

    return APPROVAL_STORE[approval_id]