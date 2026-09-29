Solution: B12 - WHICH DOOR?

Concept
Standard TCP port numbers and encrypted transport services.

Walkthrough
1. Inspect `challenge/ports.txt`.
2. Locate the line corresponding to HTTPS:
   `443/tcp open https`
3. Port is `443` and service is `https`.
4. Assemble the answer string: `port 443 https`.

Flag
port 443 https
