**Solution: I03 - THE FILE THAT PRETENDS**

**Concept**  
Magic bytes and file signature identification.

**Walkthrough**  
1. Check `challenge/notes.txt` using the `file` utility:
   ```bash
   file challenge/notes.txt
   ```
2. The file is identified as a PNG image despite the `.txt` extension.
3. Extract embedded ASCII strings:
   ```bash
   strings challenge/notes.txt | grep "flag{"
   ```
4. Output: `flag{dont_trust_extensions}`.

**Flag**  
`flag{dont_trust_extensions}`
