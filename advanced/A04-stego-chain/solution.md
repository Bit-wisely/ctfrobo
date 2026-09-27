Solution: A04 - STEGO CHAIN

Concept  
Layered steganography: LSB extraction followed by Base64 payload decoding.

Walkthrough  
1. Extract LSB data from `challenge/evidence.png`:
   `ZmxhZ3tzdGVnb19jaGFpbl9kZWNvZGVkfQ==`
2. Base64-decode the extracted string:
   ```bash
   echo "ZmxhZ3tzdGVnb19jaGFpbl9kZWNvZGVkfQ==" | base64 -d
   ```
3. Flag recovered: `flag{stego_chain_decoded}`.

Flag  
`flag{stego_chain_decoded}`
