**A04 - STEGO CHAIN**

**Points**: 400  
**Category**: Advanced / Steganography  

**Challenge Overview**  
Multi-stage steganography challenges combine multiple encoding and concealment layers. In this challenge, raw least-significant-bit extraction from pixel data reveals an intermediate Base64 token rather than cleartext. Decoding the secondary format yields the final flag.

**Participant Question**  
The picture is only the beginning. Whatever you find inside it will lead somewhere else.

**Clue**  
Extract the LSB data stream from `evidence.png`, then Base64-decode the resulting string.

**Challenge Files**  
- `challenge/evidence.png`
- `challenge/decode_helper.py`

**Flag Format**  
`flag{...}`
