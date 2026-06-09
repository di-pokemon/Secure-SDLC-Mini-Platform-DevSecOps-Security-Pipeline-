import subprocess

def run_bandit():
    result = subprocess.run(["bandit", "-r", "app"], capture_output=True, text=True)
    return result.stdout