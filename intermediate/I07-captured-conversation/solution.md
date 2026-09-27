Solution: I07 - THE CAPTURED CONVERSATION

Concept  
Cleartext HTTP traffic analysis and credential leakage.

Walkthrough  
1. Inspect `challenge/capture.txt`.
2. Locate the GET request containing the secret parameter:
   ```http
   GET /api/v1/vault/session?token=flag{secret_token_in_traffic} HTTP/1.1
   ```
3. Extract the token value.

Flag  
`flag{secret_token_in_traffic}`
