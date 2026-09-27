A12 - JWT

Points: 20
Category: Advanced / JWT Security  

Challenge Overview  
JSON Web Tokens (JWT) are self-contained security tokens consisting of a header, payload, and cryptographic signature encoded in base64url format. A critical implementation vulnerability occurs when a JWT library or custom verification logic trusts the `alg` header parameter when set to `"none"`, accepting unsigned tokens as valid.

Participant Question  
The website gave you a token. It looks complicated. But complicated does not always mean secure.

Clue  
Craft an unsigned JWT with header `{"alg": "none", "typ": "JWT"}` and payload `{"user": "admin", "role": "admin"}`. Leave the signature segment empty.

Challenge Files  
- `challenge/app/app.py`

Flag Format  
`flag{...}`
