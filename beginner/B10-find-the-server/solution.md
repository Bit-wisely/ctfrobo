Solution: B10 - FIND THE SERVER

Concept  
IPv4 subnetting and DNS hostname correlation.

Walkthrough  
1. Inspect `challenge/clues.txt`. The clues identify the target server as `vault.internal` on the `192.168.10.0/24` subnet.
2. Inspect `challenge/network.txt`:
   `vault.internal 52:54:00:12:34:56 192.168.10.45`
3. Convert IP `192.168.10.45` to underscore-delimited format.

Flag  
`flag{ip_192_168_10_45}`
