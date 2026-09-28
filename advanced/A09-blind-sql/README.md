A09 - BLIND SQL

Points: 20
Category: Advanced / Blind SQL Injection

Scenario
A web application queries a backend database based on user input, but its interface only returns boolean indicators rather than raw record data or SQL error messages.

Objective
Construct conditional blind SQL injection payloads to infer and reconstruct the hidden secret character by character.

Challenge Files
- `challenge/app/app.py`
- `challenge/app/database.sql`
- `challenge/app/exploit_demo.py`

Flag Format
`flag{...}`
