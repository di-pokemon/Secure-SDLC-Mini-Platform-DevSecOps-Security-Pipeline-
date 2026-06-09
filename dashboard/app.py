from flask import Flask, jsonify
import json
from pathlib import Path

app = Flask(__name__)


@app.route("/dashboard")
def dashboard():
    repo_root = Path(__file__).resolve().parent.parent
    report_path = repo_root / "reports" / "scan_results.json"
    with report_path.open() as f:
        data = json.load(f)
    return jsonify(data)


if __name__ == "__main__":
    app.run(port=5001)