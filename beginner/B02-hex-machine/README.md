# B02 - HEX MACHINE

| Attribute | Details |
| :--- | :--- |
| **Points** | 5 |
| **Category** | Beginner / Data Representation |
| **Difficulty** | Introductory |

---

## Scenario
A legacy embedded device diagnostic interface prints raw memory values upon startup. The engineers documented that the machine dumps a sequence of two-digit byte values before initializing the main subsystem. You must convert these raw hexadecimal values back into plain text using manual lookup or terminal commands to identify the verification passphrase.

## Objective
Execute the diagnostic program or inspect the byte sequences in `challenge/`, then decode the hexadecimal pairs into ASCII characters.

## Challenge Files
- `challenge/hexmachine.py` — Python script emitting the hex tokens
- `challenge/hexmachine.c` — C implementation of the diagnostic output

## Execution Reference
```bash
python3 challenge/hexmachine.py
# or compile C version:
gcc challenge/hexmachine.c -o hexmachine && ./hexmachine
```

## Submission Format
Submit the recovered plaintext string directly (e.g. `secret_text_here`).
