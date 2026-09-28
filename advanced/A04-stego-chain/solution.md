Solution: A04 - STEGO CHAIN

Concept  
Layered steganography: LSB extraction followed by Base64 payload decoding.

Walkthrough  
1. Extract LSB data from `challenge/evidence.png`:
   `ZmxhZ3tzdGVnbyBjaGFpbiBkZWNvZGVkfQ==`
2. Base64-decode the extracted string:
   ```bash
   echo "ZmxhZ3tzdGVnbyBjaGFpbiBkZWNvZGVkfQ==" | base64 -d
   ```
3. Flag recovered: `flag{stego chain decoded}`.

Flag  
`flag{stego chain decoded}`
