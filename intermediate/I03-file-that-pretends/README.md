**I03 - THE FILE THAT PRETENDS**

**Points**: 250  
**Category**: Intermediate / File Signatures  

**Challenge Overview**  
Operating systems and analysts cannot rely solely on file extensions (`.txt`, `.jpg`, `.pdf`) to determine the true nature of a file. The first few bytes of any file, known as magic bytes or file signatures, identify the actual file format. Disguising binaries or images as plain text files is a common evasion technique.

**Participant Question**  
The filename says one thing. The file itself says something else. Which one should you trust?

**Clue**  
Inspect the file with the `file` utility or check the opening magic bytes (`89 50 4E 47`).

**Challenge Files**  
- `challenge/notes.txt`

**Flag Format**  
`flag{...}`
