**Solution: B04 - THE FILE THAT ISN'T THERE**

**Concept**  
Linux filesystem hidden dotfiles and discovery.

**Walkthrough**  
1. Navigate into `challenge/evidence/`.
2. List all directory contents including hidden dotfiles:
   ```bash
   ls -la
   ```
3. Locate `.clue` in the output.
4. Read `.clue`:
   ```bash
   cat .clue
   ```

**Flag**  
`flag{not_every_file_is_visible}`
