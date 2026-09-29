# B04 - HIDDEN IN PLAIN SIGHT

| Attribute | Details |
| :--- | :--- |
| **Points** | 5 |
| **Category** | Beginner / Linux Filesystem |
| **Difficulty** | Introductory |

---

## Scenario
A junior investigator conducted an initial sweep of an evidence folder extracted from a compromised workstation and concluded that the directory only contained uninteresting boilerplate notes. However, forensic protocol requires verifying that all filesystem artifacts—including entries obscured by operating system defaults—have been thoroughly reviewed.

## Objective
Explore the directory structure inside `challenge/case/`, uncover any hidden directories or files, and retrieve the flag message.

## Challenge Files
- `challenge/case/` — Directory containing evidence files and directories

## Execution Reference
```bash
# Navigate to challenge directory:
cd challenge/case
```

## Submission Format
Submit the recovered plaintext string directly (e.g. `secret_text_here`).
