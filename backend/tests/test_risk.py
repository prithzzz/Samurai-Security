from app.risk.pipeline import run_risk_pipeline

def test_pipeline():
    sample = {
        "leakage_score": 0.9,
        "bias_flag": True,
        "jailbreak_detected": True,
        "memory_attack": False,
        "responses": [
            "Safe response",
            "Unsafe answer",
            "Detailed harmful output"
        ]
    }

    result = run_risk_pipeline("TestModel", sample)

    assert "risk_score" in result
    assert result["risk_level"] in ["LOW", "MEDIUM", "HIGH"]