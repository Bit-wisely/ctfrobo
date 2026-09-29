# B14 - THE DATABASE KNOWS

| Attribute | Details |
| :--- | :--- |
| **Points** | 5 |
| **Category** | Beginner / Relational Databases |
| **Difficulty** | Intermediate Beginner |

---

## Scenario
An incident response unit isolated a forensic database snapshot (`company_vault.db`) from a compromised corporate infrastructure server. Multiple decoy entries and routine logs populate the database. Triage notes from the Security Operations Center (SOC) indicate the following forensic parameters:
- The target authorization event executed the action: `OVERRIDE_AUTH`.
- The user account was assigned to the `Cyber Defense` department.
- The user held a security clearance of `Level-5`.
- The corresponding audit token for this event was archived in the `classified_vault` table.

## Objective
Query the relational SQLite database `challenge/company_vault.db` using SQL joins and filtering conditions to identify the privileged access event and retrieve the secret token.

## Challenge Files
- `challenge/company_vault.db` — SQLite 3 relational database containing multiple interconnected tables

## Execution Reference
```bash
# Query using sqlite3 CLI:
sqlite3 challenge/company_vault.db
# or via Python:
python3 -c "import sqlite3; conn=sqlite3.connect('challenge/company_vault.db'); ..."
```

## Submission Format
Submit the recovered plaintext string directly (e.g. `secret_text_here`).
