Secure SDLC Threat Model (STRIDE)

System: Web Application + API + Database

1. Spoofing
- Weak authentication could allow impersonation

2. Tampering
- API requests may be modified without validation

3. Repudiation
- Lack of logging may prevent tracking actions

4. Information Disclosure
- Sensitive API data exposed via endpoints

5. Denial of Service
- No rate limiting may allow API flooding

6. Elevation of Privilege
- Improper access control in endpoints