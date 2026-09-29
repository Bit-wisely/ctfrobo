# B08 - WHICH DOOR?

| Attribute | Details |
| :--- | :--- |
| **Points** | 5 |
| **Category** | Beginner / Networking |
| **Difficulty** | Introductory |

---

## Scenario
A network reconnaissance scan was executed against an edge server (`gateway.internal`). The security team captured the port table and version banners for all open TCP sockets. Security compliance mandates verifying that encrypted web traffic is actively offered on the appropriate well-known port.

## Objective
Analyze the reconnaissance report in `challenge/ports.txt`, identify the port and banner corresponding to the secure HTTPS service, and retrieve the flag token.

## Challenge Files
- `challenge/ports.txt` — Port scan log with port numbers, service types, and version banners

## Submission Format
Submit the recovered plaintext string directly (e.g. `secret_text_here`).
