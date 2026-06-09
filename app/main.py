from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def home():
    return jsonify({
        "message": "Secure SDLC Platform Running",
        "status": "secure"
    })


@app.route("/api/data")
def data():
    return jsonify({
        "data": "sensitive information placeholder"
    })


if __name__ == "__main__":
    import os

    # Control debug/host/port using environment variables for safer defaults
    debug = os.getenv("FLASK_DEBUG", "False").lower() in ("1", "true", "yes")
    host = os.getenv("FLASK_HOST", "127.0.0.1")
    port = int(os.getenv("FLASK_PORT", "5000"))

    app.run(host=host, port=port, debug=debug)