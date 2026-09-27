Solution: B13 - TWO SWITCHES

Concept  
Bitwise XOR cipher and symmetric reversibility.

Walkthrough  
1. Review the XOR truth table in `challenge/switches.txt`.
2. Compute `c ^ 66` for each ciphertext integer in the array:

```python
cipher = [36, 46, 35, 37, 57, 58, 45, 48, 29, 43, 49, 29, 48, 39, 52, 39, 48, 49, 43, 32, 46, 39, 63]
key = 66
flag = "".join(chr(c ^ key) for c in cipher)
print(flag)
```

Flag  
`flag{xor_is_reversible}`
