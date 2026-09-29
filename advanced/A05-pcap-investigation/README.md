# A05 - PCAP INVESTIGATION

Points: 20
Category: Advanced / Deep Network Forensics

## Scenario
An intrusion detection system recorded raw network traffic during a targeted data exfiltration incident. The attacker evaded naive signature detection by fragmenting the exfiltrated data across an arbitrary TCP stream out-of-order, while negotiating extraction keys via a separate C2 session.

## Objective
Correlate the concurrent network streams across different IP endpoints and ports in `capture.pcap`. Reconstruct the session parameters, reassemble the fragmented payload blocks in order, and decrypt the exfiltrated flag.

Execution Reference
To run Python files: python filename.py
To compile and run C files: gcc filename.c -o output && ./output
Wireshark / TShark: wireshark challenge/capture.pcap
