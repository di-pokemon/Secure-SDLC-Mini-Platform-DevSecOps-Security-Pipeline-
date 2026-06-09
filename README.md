
# Secure SDLC Mini Platform

## Overview
A DevSecOps simulation project demonstrating Secure Software Development Lifecycle (SSDLC) with automated security scanning and risk analysis.

## Features
- Flask secure API
- SAST scanning (Bandit)
- Dependency scanning (pip-audit)
- Secret scanning (Trufflehog optional)
- Risk scoring engine
- Security dashboard
- CI/CD pipeline (GitHub Actions)

## Architecture
<img width="1376" height="768" alt="secure SDLC" src="https://github.com/user-attachments/assets/3841714b-798c-4569-bc38-a191a671cc7a" />

## How to Run
```bash
pip install -r requirements.txt
python app/main.py
