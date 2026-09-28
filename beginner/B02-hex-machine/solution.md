Solution: B02 - HEX MACHINE

Concept  
Hexadecimal encoding and byte decoding.

Walkthrough  
1. Inspect `challenge/output.txt`:
   `66 6c 61 67 7b 68 65 78 20 6d 61 63 68 69 6e 65 7d`
2. Map each hexadecimal byte to its ASCII equivalent:
   - `0x66` -> 'f'
   - `0x6c` -> 'l'
   - `0x61` -> 'a'
   - `0x67` -> 'g'
   - `0x7b` -> '{'
   - `0x68` -> 'h'
   - `0x65` -> 'e'
   - `0x78` -> 'x'
   - `0x20` -> ' '
   - `0x6d` -> 'm'
   - `0x61` -> 'a'
   - `0x63` -> 'c'
   - `0x68` -> 'h'
   - `0x69` -> 'i'
   - `0x6e` -> 'n'
   - `0x65` -> 'e'
   - `0x7d` -> '}'
3. The resulting string is `flag{hex machine}`.

Flag  
`flag{hex machine}`
