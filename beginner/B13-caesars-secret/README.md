# B13 - CAESAR'S SECRET

| Attribute | Details |
| :--- | :--- |
| **Points** | 5 |
| **Category** | Beginner / Cryptography |
| **Difficulty** | Intermediate Beginner |

---

## Scenario
A historical tactical dispatch was intercepted on an outdated radio frequency. The communications officer used an ancient rotational shift technique to disguise the contents of the transmission, believing that displacing the letters along the alphabet would be sufficient to prevent interception.

## Objective
Analyze the encrypted message in `challenge/message.txt`, identify the rotational offset, and recover the flag.

## Challenge Files
- `challenge/message.txt` — The intercepted Caesar ciphertext
- `challenge/converter.py` — An optional interactive tool for testing rotational shifts

## Execution Reference
```bash
python3 challenge/converter.py
```

## Submission Format
Submit the recovered plaintext string directly (e.g. `secret_text_here`).
