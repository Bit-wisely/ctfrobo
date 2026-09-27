Solution: I01 - BASE64 ISN'T ENCRYPTION

Concept  
Base64 encoding vs cryptographic encryption.

Walkthrough  
1. Inspect `challenge/message.txt`:
   `ZmxhZ3tiYXNlNjR9`
2. Decode the Base64 string:
   ```bash
   echo "ZmxhZ3tiYXNlNjR9" | base64 -d
   ```
3. Flag is retrieved: `flag{base64}`.

Flag  
`flag{base64}`
