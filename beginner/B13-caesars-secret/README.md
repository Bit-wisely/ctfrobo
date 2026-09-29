# B13 - CAESAR'S SECRET

| Attribute | Details |
| :--- | :--- |
| **Points** | 5 |
| **Category** | Beginner / Cryptography |
| **Difficulty** | Intermediate Beginner |

---

## Scenario
A lengthy tactical dispatch from an adversary command outpost was intercepted over an encrypted radio telemetry band. The sender utilized a classical rotational shift cipher (Caesar cipher) across the entire dispatch. Because the message is sufficiently long and preserves common English grammar patterns, frequency analysis of the characters can expose the shift key.

## Objective
Analyze the encrypted dispatch in `challenge/message.txt`, deduce the Caesar shift key using frequency analysis, decode the message, and retrieve the uppercase authentication passcode.

## Challenge Files
- `challenge/message.txt` — Intercepted tactical ciphertext dispatch

## Submission Format
Submit the recovered uppercase flag string directly (e.g. `UPPERCASE_FLAG_HERE`).
