# Solution: B15 - TWO SWITCHES

## Concept
The bitwise exclusive-OR (XOR) operation $(\oplus)$ is self-inverting: $(P \oplus K) \oplus K = P$. Applying the single-byte key to the ciphertext numbers reverses the mask to produce original character codes.

## Walkthrough
1. Inspect `challenge/switches.txt`:
   - Operation: Bitwise XOR
   - Cipher Key: 66
   - Ciphertext bytes: `50 35 48 43 54 59 29 37 35 54 39 29 43 44 52 39 48 54 39 38 29 116 113`
2. Decrypt each byte using the key in Python:
   ```python
   cipher = [50, 35, 48, 43, 54, 59, 29, 37, 35, 54, 39, 29, 43, 44, 52, 39, 48, 54, 39, 38, 29, 116, 113]
   key = 66
   flag = "".join(chr(c ^ key) for c in cipher)
   print(flag)
   ```
3. Recover the decoded text:
   ```
   parity_gate_inverted_63
   ```

## Flag
`parity_gate_inverted_63`
