**Solution: I06 - SMALLEST BITS**

**Concept**  
Least Significant Bit (LSB) steganography extraction.

**Walkthrough**  
1. Analyze `challenge/image.png` using `zsteg`:
   ```bash
   zsteg challenge/image.png
   ```
2. Or use Python to iterate through the bytes, collecting `b & 1` and assembling 8-bit groups into ASCII characters.
3. The extracted payload is `flag{lsb_bits_unlocked}`.

**Flag**  
`flag{lsb_bits_unlocked}`
