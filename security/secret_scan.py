import subprocess

def run_trufflehog():
    try:
        result = subprocess.run(
            ["trufflehog", "filesystem", "."],
            capture_output=True,
            text=True
        )
        return result.stdout
    except Exception:
        return "Trufflehog not installed or scan failed"