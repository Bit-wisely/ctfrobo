Solution: B03 - THE LAST ONE OUT

Concept  
Stack operations and LIFO execution.

Walkthrough  
1. Follow the push operations in `challenge/locker.c` or `challenge/locker.py`:
   - `PUSH 80` -> 'P'
   - `PUSH 65` -> 'A'
   - `PUSH 71` -> 'G'
   - `PUSH 69` -> 'E'
2. Combining the pushed characters in original insertion order reveals the word `PAGE`.
3. Open `challenge/page.txt` to retrieve the flag.

Flag  
`flag{stack_escape}`
