# B07 - FIND THE PROCESS

| Attribute | Details |
| :--- | :--- |
| **Points** | 5 |
| **Category** | Beginner / Linux Administration |
| **Difficulty** | Intermediate Beginner |

---

## Scenario
A system administrator captured a snapshot of all active processes on a workstation (`processes.txt`) before isolating the terminal. While the majority of entries represent legitimate system daemons and standard desktop software, security monitoring indicated that an interactive user shell spawned a rogue process from an unusual location on the disk.

## Objective
Analyze the process table in `challenge/processes.txt`, locate the rogue process spawned under the interactive user shell, and identify its Process ID (PID).

## Challenge Files
- `challenge/processes.txt` — Process snapshot table with PID, PPID, User, and Command columns

## Submission Format
Submit the numeric Process ID directly (e.g. `1234`).
