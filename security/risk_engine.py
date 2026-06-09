import json
import os

def calculate_risk():

    # Simple demo logic (you can improve later)
    vulnerabilities = {
        "sast_issues": 3,
        "dependency_issues": 2,
        "secret_issues": 1
    }

    score = (
        vulnerabilities["sast_issues"] * 5 +
        vulnerabilities["dependency_issues"] * 7 +
        vulnerabilities["secret_issues"] * 10
    )

    if score < 20:
        level = "LOW"
    elif score < 50:
        level = "MEDIUM"
    else:
        level = "HIGH"

    report = {
        "risk_score": score,
        "risk_level": level,
        "breakdown": vulnerabilities,
        "recommendation": "Fix highest severity issues first"
    }

    os.makedirs("reports", exist_ok=True)

    with open("reports/scan_results.json", "w") as f:
        json.dump(report, f, indent=4)

    return report


if __name__ == "__main__":
    print(calculate_risk())