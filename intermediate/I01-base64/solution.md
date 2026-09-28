Solution: I01 - BASE64 ISN'T ENCRYPTION

Concept  
Base64 encoding vs cryptographic encryption.

Walkthrough  
1. Inspect `challenge/message.txt`:
   `YmFzZTY0`
2. Decode the Base64 string:
   ```bash
   echo "YmFzZTY0" | base64 -d
   ```
3. Flag is retrieved: `base64`.

Flag  
`base64`
