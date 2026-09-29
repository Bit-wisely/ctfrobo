# B09 - FIND THE SERVER

| Attribute | Details |
| :--- | :--- |
| **Points** | 5 |
| **Category** | Beginner / Networking |
| **Difficulty** | Intermediate Beginner |

---

## Scenario
A security analyst investigating lateral movement across an enterprise network recovered an inventory table of hosts along with field notes from the network engineering team. The incident notes single out a confidential vault host operating on an isolated internal subnet.

## Objective
Analyze `challenge/clues.txt` and `challenge/network.txt` to identify the IP address of the target vault host and formulate the flag string.

## Challenge Files
- `challenge/clues.txt` — Forensic notes regarding the target hostname and subnet
- `challenge/network.txt` — Network host table containing hostnames, MACs, and IP addresses

## Submission Format
Submit the answer in the format specified in `clues.txt`: `host_<name>_<ip_with_underscores>` (e.g. `host_vault_192_168_10_45`).
