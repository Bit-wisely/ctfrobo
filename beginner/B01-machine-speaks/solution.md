Solution: B01 - THE MACHINE SPEAKS

Concept  
Binary representation and conversion to ASCII text.

Walkthrough  
1. Inspect the binary output lines from the challenge:
   - `01100010` -> decimal 98  -> 'b'
   - `01101001` -> decimal 105 -> 'i'
   - `01101110` -> decimal 110 -> 'n'
   - `01100001` -> decimal 97  -> 'a'
   - `01110010` -> decimal 114 -> 'r'
   - `01111001` -> decimal 121 -> 'y'
   - `00100000` -> decimal 32  -> ' '
   - `01110011` -> decimal 115 -> 's'
   - `01110000` -> decimal 112 -> 'p'
   - `01100101` -> decimal 101 -> 'e'
   - `01100001` -> decimal 97  -> 'a'
   - `01101011` -> decimal 107 -> 'k'
   - `01110011` -> decimal 115 -> 's'
2. Reassemble all characters sequentially: `binary speaks`.

Flag  
`binary speaks`
