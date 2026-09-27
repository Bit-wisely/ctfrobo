**Solution: A02 - THE PROGRAM HAS A BACKDOOR**

**Concept**  
Static control flow analysis and discovery of hidden command branches.

**Walkthrough**  
1. Inspect `challenge/program.c`.
2. Locate the hidden conditional branch:
   ```c
   else if (strcmp(cmd, "backdoor") == 0) {
       secret_backdoor();
   }
   ```
3. Type `backdoor` into the application prompt.
4. Output: `flag{backdoor_found}`.

**Flag**  
`flag{backdoor_found}`
