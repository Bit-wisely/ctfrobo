A12 - JWT

Points: 20
Category: Advanced / JWT Security

Scenario
A web service authenticates API requests using JSON Web Tokens (JWT). The token verification mechanism improperly trusts token headers without enforcing valid cryptographic signatures.

Objective
Forge an unauthorized JWT with elevated privileges to bypass authentication and retrieve the flag.

Challenge Files
- `challenge/app/app.py`

Flag Format
`flag{...}`
