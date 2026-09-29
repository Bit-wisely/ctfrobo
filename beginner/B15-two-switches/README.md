# B15 - TWO SWITCHES

| Attribute | Details |
| :--- | :--- |
| **Points** | 5 |
| **Category** | Beginner / Cryptography |
| **Difficulty** | Intermediate Beginner |

---

## Scenario
An industrial field transponder encodes alert messages across an electronic switch matrix before transmitting them over sensor lines. An electrical reference card was left behind showing how the circuit switches combine signal and key inputs. The transmitted numbers represent decimal byte values masked by a single-byte secret key.

## Objective
Analyze `challenge/switches.txt`, reverse the reversible logic transformation using the provided cipher key, and recover the plaintext flag.

## Challenge Files
- `challenge/switches.txt` — Logic gate reference card, cipher key, and ciphertext integer values
- `challenge/converter.py` — Optional helper script for testing XOR operations

## Execution Reference
```bash
python3 challenge/converter.py
```

## Submission Format
Submit the recovered plaintext string directly (e.g. `secret_text_here`).
