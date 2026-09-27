**A11 - PATH TRAVERSAL**

**Points**: 500  
**Category**: Advanced / Web Path Traversal  

**Challenge Overview**  
Path Traversal (also known as Directory Traversal or Dot-Dot-Slash) enables attackers to read arbitrary files on the server running an application. When an application constructs file paths using user-controlled parameters without canonicalizing or restricting paths to a safe base directory, dot-dot-slash (`../`) sequences break out into restricted folders.

**Participant Question**  
You are allowed to download files. The server says you can only access one directory. But the filesystem may disagree.

**Clue**  
Use `../` sequences in the `file` query parameter (e.g. `/download?file=../secret/flag.txt`) to navigate up out of the `public/` directory.

**Challenge Files**  
- `challenge/app/app.py`
- `challenge/app/public/sample.txt`
- `challenge/app/secret/flag.txt`

**Flag Format**  
`flag{...}`
