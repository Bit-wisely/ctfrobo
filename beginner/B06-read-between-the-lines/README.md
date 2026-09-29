# B06 - READ BETWEEN THE LINES

| Attribute | Details |
| :--- | :--- |
| **Points** | 5 |
| **Category** | Beginner / Linux Utilities |
| **Difficulty** | Introductory |

---

## Scenario
A suspicious event occurred on a workstation, leaving behind a raw system log file containing hundreds of legitimate routine daemon messages. Incident responders suspect the intruder or a rogue script left a breadcrumb or custom status message hidden directly among the routine log records.

## Objective
Search through `challenge/logs/system.log` to isolate the anomalous entry and recover the hidden flag.

## Challenge Files
- `challenge/logs/system.log` — Operating system log file

## Execution Reference
```bash
# Navigate to challenge directory:
cd challenge/logs
```

## Submission Format
Submit the recovered plaintext string directly (e.g. `secret_text_here`).
