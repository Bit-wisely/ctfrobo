Solution: I03 - THE FILE THAT PRETENDS

Concept  
Magic bytes and file signature identification.

Walkthrough  
1. Check `challenge/notes.txt` using the `file` utility:
   ```bash
   file challenge/notes.txt
   ```
2. The file is identified as a PNG image despite the `.txt` extension.
3. Extract embedded ASCII strings:
   ```bash
   strings challenge/notes.txt
   ```
4. Locate the text metadata string: `dont trust extensions`.

Flag  
`dont trust extensions`
