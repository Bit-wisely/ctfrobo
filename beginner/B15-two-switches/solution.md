# Solution: B15 - TWO SWITCHES

## Concept
The bitwise exclusive-OR (XOR) operation $(\oplus)$ is self-inverting: $(P \oplus K) \oplus K = P$. Applying the integer key to each decimal ciphertext value reverses the transformation to recover standard ASCII character codes.

## Walkthrough
1. Inspect `challenge/switches.txt`:
   - Operation: Bitwise XOR
   - Cipher Key: `66`
   - Ciphertext bytes (decimal): `50 35 48 43 54 59 29 37 35 54 39 29 43 44 52 39 48 54 39 38 29 116 113`
2. Decrypt each decimal value using the key in Python:
   ```python
   cipher = [50, 35, 48, 43, 54, 59, 29, 37, 35, 54, 39, 29, 43, 44, 52, 39, 48, 54, 39, 38, 29, 116, 113]
   key = 66
   flag = "".join(chr(c ^ key) for c in cipher)
   print(flag)
   ```
3. Or run `python3 challenge/converter.py`, choose Option 1, and paste the numbers and key.
4. Clean ASCII output produced:
   ```
   parity_gate_inverted_63
   ```

## Flag
`parity_gate_inverted_63`
