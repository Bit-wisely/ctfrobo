# B03 - BASE64 ISN'T ENCRYPTION

| Attribute | Details |
| :--- | :--- |
| **Points** | 5 |
| **Category** | Beginner / Data Representation |
| **Difficulty** | Introductory |

---

## Scenario
During a security review of internal network traffic, you intercept a data transmission sent between two development workstations. A developer left a note asserting that the secret token was "strongly encrypted" before transmission. However, examining the payload reveals regular alphanumeric characters with padding characters at the end, suggesting an encoding rather than true cryptographic protection.

## Objective
Analyze the encoded string provided in `challenge/message.txt` and recover the underlying plaintext secret using manual lookup or command-line utilities.

## Challenge Files
- `challenge/message.txt` — The intercepted data string

## Submission Format
Submit the recovered plaintext string directly (e.g. `secret_text_here`).
