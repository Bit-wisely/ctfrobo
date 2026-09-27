Solution: B09 - WHICH DOOR?

Concept  
Standard TCP port numbers and encrypted transport services.

Walkthrough  
1. Inspect `challenge/ports.txt`.
2. Locate the line corresponding to HTTPS:
   `443/tcp open https`
3. Port is `443` and service is `https`.
4. Wrap in flag format: `flag{port_443_https}`.

Flag  
`flag{port_443_https}`
