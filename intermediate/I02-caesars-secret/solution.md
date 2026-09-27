Solution: I02 - CAESAR'S SECRET

Concept  
Caesar cipher monoalphabetic substitution cryptanalysis.

Walkthrough  
1. Inspect `challenge/message.txt`:
   `IODJ{FDHVDU}`
2. Identify the shift: `I` (9) - `F` (6) = 3 positions.
3. Shift all characters back by 3:
   - `I` -> 'f'
   - `O` -> 'l'
   - `D` -> 'a'
   - `J` -> 'g'
   - `F` -> 'c'
   - `D` -> 'a'
   - `H` -> 'e'
   - `V` -> 's'
   - `D` -> 'a'
   - `U` -> 'r'

Flag  
`flag{caesar}`
