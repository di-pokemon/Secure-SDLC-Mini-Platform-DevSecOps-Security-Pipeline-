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
Developer → GitHub → CI/CD → Security Scans → Risk Engine → Dashboard

## How to Run
```bash
pip install -r requirements.txt
python app/main.py