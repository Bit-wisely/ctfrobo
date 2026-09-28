A06 - DNS EXFILTRATION

Points: 20
Category: Advanced / DNS Tunneling

Scenario
An external adversary bypassed perimeter egress controls by encoding stolen assets into recursive DNS queries. The DNS query logs hold the fragmented pieces of the exfiltrated transmission.

Objective
Filter the DNS query records, extract the ordered payload segments, and reassemble the original flag.

Challenge Files
- `challenge/dns.log`

Flag Format
`flag{...}`
