# B14 - THE DATABASE KNOWS

| Attribute | Details |
| :--- | :--- |
| **Points** | 5 |
| **Category** | Beginner / Databases |
| **Difficulty** | Intermediate Beginner |

---

## Scenario
A backend system export was acquired from an operational database. The application team maintains user account role definitions alongside a classified vault table where administrators store sensitive operational secrets. Frontend reports redact sensitive records, but the raw SQL dump preserves the relational tables and keys.

## Objective
Inspect `challenge/database.sql` or run the database querying script in `challenge/query_db.py` to isolate the record linked to the administrative account and recover the flag.

## Challenge Files
- `challenge/database.sql` — Schema and seed data dump
- `challenge/query_db.py` — Database execution and testing helper

## Execution Reference
```bash
python3 challenge/query_db.py
```

## Submission Format
Submit the recovered plaintext string directly (e.g. `secret_text_here`).
