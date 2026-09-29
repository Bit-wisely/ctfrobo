# B03 - THE MACHINE SPEAKS

| Attribute | Details |
| :--- | :--- |
| **Points** | 5 |
| **Category** | Beginner / Data Representation |
| **Difficulty** | Introductory |

---

## Scenario
A telecommunications monitoring station captured an electrical stream from a legacy telemetry transponder. The hardware serializes its internal state directly into pulses of high and low voltages, recorded digitally as an unformatted sequence of zeroes and ones. To understand the signal's message, you must translate these binary values back to character text.

## Objective
Execute the simulation binary or script in `challenge/`, parse the 8-bit binary strings, and convert them to ASCII text.

## Challenge Files
- `challenge/speak.py` — Python transmission emulator
- `challenge/speak.c` — C transmission emulator
- `challenge/converter.py` — Optional conversion helper tool

## Execution Reference
```bash
python3 challenge/speak.py
# or compile C version:
gcc challenge/speak.c -o speak && ./speak
```

## Submission Format
Submit the recovered plaintext string directly (e.g. `secret_text_here`).
