Solution: I12 - DNS DETECTIVE

Concept  
DNS threat hunting and anomaly detection.

Walkthrough  
1. Inspect `challenge/dns.log`.
2. Locate the anomalous TXT query:
   `c2-beacon-flag-suspicious_c2_domain_found.threat-intel.xyz`
3. Extract the flag payload: `flag{suspicious c2 domain found}`.

Flag  
`flag{suspicious c2 domain found}`
