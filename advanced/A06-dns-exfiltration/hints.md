**Hints: A06 - DNS EXFILTRATION**

1. Queries sent to `exfil.domain.com` follow the format `<seq>.<hex_payload>.exfil.domain.com`.
2. Sort the queries by sequence number from `01` to `07`.
3. Concatenate the hex substrings and decode them from hex to ASCII.
