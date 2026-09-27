**A07 - COOKIE FORGERY**

**Points**: 450  
**Category**: Advanced / Web Session Security  

**Challenge Overview**  
Stateful web sessions that rely on JSON blobs stored inside client cookies must be protected with cryptographic signatures (such as HMAC). If the server trusts user-supplied JSON values directly without verifying integrity or authentication tags, users can modify their identity, role, and permission levels.

**Participant Question**  
The website gives you an identity. The website also trusts you to carry it. Can you change who it thinks you are?

**Clue**  
The session cookie is an unsigned Base64-encoded JSON string: `{"user": "guest", "role": "user"}`. Alter the role to `admin`, re-encode it in Base64, and pass it in the `Cookie` header.

**Challenge Files**  
- `challenge/app/app.py`

**Flag Format**  
`flag{...}`
