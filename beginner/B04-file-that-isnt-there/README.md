**B04 - THE FILE THAT ISN'T THERE**

**Points**: 150  
**Category**: Beginner / Linux Environment  

**Challenge Overview**  
In Unix and Linux filesystems, files or directories with a name beginning with a period (dotfiles) are hidden by default from ordinary file listing commands. Attackers and administrative scripts often utilize dotfiles to store configuration details, cache items, or concealed artifacts.

**Participant Question**  
The investigator says there are four files. You can only see three. Someone is hiding something. Find what you cannot see.

**Clue**  
Look for files that start with a period. Standard directory listings hide them unless specific flags like `-a` are applied.

**Challenge Files**  
- `challenge/evidence/report.txt`
- `challenge/evidence/notes.txt`
- `challenge/evidence/photo.jpg`

**Flag Format**  
`flag{...}`
