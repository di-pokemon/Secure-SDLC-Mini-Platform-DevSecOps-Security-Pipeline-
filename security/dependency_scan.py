import subprocess

def run_pip_audit():
    try:
        result = subprocess.run(
            ["pip-audit"],
            capture_output=True,
            text=True
        )
        return result.stdout
    except Exception as e:
        return str(e)