# B05 - PERMISSION DENIED

| Attribute | Details |
| :--- | :--- |
| **Points** | 5 |
| **Category** | Beginner / Linux Filesystem & Permissions |
| **Difficulty** | Introductory |

---

## Scenario
An automated access gateway utility (`verify_access.py`) enforces strict least-privilege security policies before decrypting internal credentials. In production environments, services like SSH and GPG reject private keys or sensitive tokens if filesystem permissions allow unauthorized users or groups to read them. When you attempt to run the validator, access is denied due to unsafe file permissions on `confidential_token.key`.

## Objective
Inspect and adjust the filesystem permissions of `challenge/confidential_token.key` using the `chmod` command to satisfy the required least-privilege policy (Owner Read/Write ONLY: `0600`), then execute `verify_access.py` to retrieve the flag.

## Challenge Files
- `challenge/confidential_token.key` — The protected credential file
- `challenge/verify_access.py` — Security policy verification script

## Execution Reference
```bash
# Check current permissions:
ls -l challenge/confidential_token.key

# Run the validator:
python3 challenge/verify_access.py
```

## Submission Format
Submit the recovered plaintext string directly (e.g. `secret_text_here`).
