Solution: B01 - THE MACHINE SPEAKS

Concept  
Binary representation and conversion to ASCII text.

Walkthrough  
1. Inspect the binary output lines provided in `challenge/output.txt`:
   - `01100110` -> decimal 102 -> 'f'
   - `01101100` -> decimal 108 -> 'l'
   - `01100001` -> decimal 97  -> 'a'
   - `01100111` -> decimal 103 -> 'g'
   - `01111011` -> decimal 123 -> '{'
   - ...
   - `01111101` -> decimal 125 -> '}'
2. Reassemble all characters sequentially.

```python
with open("output.txt") as f:
    lines = f.read().split()
flag = "".join(chr(int(b, 2)) for b in lines)
print(flag)
```

Flag  
`flag{binary_speaks}`
