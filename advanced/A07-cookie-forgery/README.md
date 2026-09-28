A07 - COOKIE FORGERY

Points: 20
Category: Advanced / Web Session Security

Scenario
A web portal issues client-side session cookies to identify users and assign role permissions. The backend application trusts the incoming cookie data without verifying its cryptographic integrity.

Objective
Analyze the structure of the session token, tamper with the privilege parameters, and gain unauthorized administrator access to claim the flag.

Challenge Files
- `challenge/app/app.py`

Flag Format
`flag{...}`
