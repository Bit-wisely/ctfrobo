**A13 - BROKEN AUTHENTICATION**

**Points**: 500  
**Category**: Advanced / Authentication Flaws  

**Challenge Overview**  
Password reset mechanisms rely on high-entropy cryptographically secure pseudorandom numbers (CSPRNG) to generate single-use recovery tokens. If an application calculates reset tokens deterministically using static salts or predictable timestamps, an attacker can precalculate the administrator's recovery token and take over the account.

**Participant Question**  
You don't have the administrator's password. But the application has another way of deciding who is allowed in. Find the mistake.

**Clue**  
The password reset token is generated deterministically as `MD5(username + "_secret_recovery_salt_2026")`. Compute the hash for user `admin` and request `/reset?token=<hash>`.

**Challenge Files**  
- `challenge/app/app.py`

**Flag Format**  
`flag{...}`
