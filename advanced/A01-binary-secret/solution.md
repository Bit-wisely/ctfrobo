# Solution: A01 - THE BINARY SECRET

## Concept
Reverse engineering byte comparison routines and reversing XOR transformations.

## Walkthrough
1. Inspect the comparison logic in `challenge/mystery.c`:
   `((unsigned char)(input[i] ^ 0x37) == expected[i])`
2. Decrypt the `expected` array with key `0x37`:
   ```python
   expected = [0x4d, 0x52, 0x56, 0x53, 0x17, 0x4b, 0x5f, 0x52, 0x17, 0x55, 0x5e, 0x59, 0x56, 0x4d, 0x46]
   flag = "".join(chr(b ^ 0x37) for b in expected)
   print(flag)
   ```
3. Flag recovered: `read the binary`.

## Flag
`read the binary`
