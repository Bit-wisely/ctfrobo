**I12 - DNS DETECTIVE**

**Points**: 350  
**Category**: Intermediate / DNS Forensics  

**Challenge Overview**  
Domain Name System (DNS) logs provide essential telemetry for tracking network activity. Malware and Advanced Persistent Threats (APTs) often communicate with Command and Control (C2) servers or execute data staging using unusual DNS queries and anomalous record types (such as TXT records).

**Participant Question**  
Most of these requests are normal. One of them isn't. Find the strange one.

**Clue**  
Look through the DNS query logs for anomalous TXT record types and non-standard domain names containing `c2-beacon`.

**Challenge Files**  
- `challenge/dns.log`

**Flag Format**  
`flag{...}`
