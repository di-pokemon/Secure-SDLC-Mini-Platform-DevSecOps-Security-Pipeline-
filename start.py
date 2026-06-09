#!/usr/bin/env python3
"""Start the Flask app on a free localhost port if desired port is in use.

Usage: python start.py
You can set FLASK_PORT to force a port. By default it picks a free 127.0.0.1 port.
"""
import os
import socket
import sys


def find_free_port() -> int:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(("127.0.0.1", 0))
    port = s.getsockname()[1]
    s.close()
    return port


def main():
    port = os.getenv("FLASK_PORT")
    if port is None or port == "":
        port = str(find_free_port())

    os.environ["FLASK_PORT"] = port
    os.environ.setdefault("FLASK_DEBUG", "False")

    print(f"Starting app on http://127.0.0.1:{port} (FLASK_DEBUG={os.environ['FLASK_DEBUG']})")

    # Exec the main app so signals/ctrl-c behave normally
    python = sys.executable
    os.execv(python, [python, os.path.join("app", "main.py")])


if __name__ == "__main__":
    main()
