# B12 - THE INBOX TRAP

| Attribute | Details |
| :--- | :--- |
| **Points** | 5 |
| **Category** | Beginner / Forensics |
| **Difficulty** | Intermediate Beginner |

---

## Scenario
A corporate mailbox on an executive's workstation was exported as part of an incident response triage (`email_dump.txt`). The archive includes routine messages from colleagues, automated system status alerts, promotional mailings, and a targeted phishing campaign. The security team needs to pinpoint the specific lure that compromised the user's workstation.

## Objective
Analyze the message corpus in `challenge/email_dump.txt`, identify the fraudulent verification lure, and extract its campaign tracking reference ID as the flag.

## Challenge Files
- `challenge/email_dump.txt` — Full email inbox dump containing message headers and body contents

## Submission Format
Submit the recovered reference string directly (e.g. `secret_text_here`).
