Solution: B04 - CAESAR'S SECRET

Concept
Caesar cipher monoalphabetic substitution cryptanalysis.

Walkthrough
1. Inspect `challenge/message.txt`:
   `FDHVDU`
2. Identify the shift: rotating back by 3 positions (or +23):
   - `F` -> 'c'
   - `D` -> 'a'
   - `H` -> 'e'
   - `V` -> 's'
   - `D` -> 'a'
   - `U` -> 'r'
3. Flag is retrieved: `caesar`.

Flag
caesar
