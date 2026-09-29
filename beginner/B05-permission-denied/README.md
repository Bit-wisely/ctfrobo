# B05 - PERMISSION DENIED

| Attribute | Details |
| :--- | :--- |
| **Points** | 5 |
| **Category** | Beginner / Linux Filesystem |
| **Difficulty** | Introductory |

---

## Scenario
A security auditor stored critical notes in an audit directory alongside sensitive configuration files and private keys. The files have varying access permissions configured to prevent unauthorized viewing. Most files are restricted to root or specialized system service accounts, but one public report was left accessible.

## Objective
Inspect the file permissions in `challenge/audit/`, identify which document can be read by standard users, and retrieve the flag.

## Challenge Files
- `challenge/audit/` — Directory containing various configuration and report files

## Execution Reference
```bash
# Navigate to challenge directory:
cd challenge/audit
```

## Submission Format
Submit the recovered plaintext string directly (e.g. `secret_text_here`).
