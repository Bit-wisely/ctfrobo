# Solution: A04 - STEGO CHAIN

## Concept
Layered steganography: LSB extraction followed by Base64 payload decoding.

## Walkthrough
1. Extract LSB data from `challenge/evidence.png`:
   `c3RlZ28gY2hhaW4gZGVjb2RlZA==`
2. Base64-decode the extracted string:
   ```bash
   echo "c3RlZ28gY2hhaW4gZGVjb2RlZA==" | base64 -d
   ```
3. Flag recovered: `stego chain decoded`.

## Flag
`stego chain decoded`
