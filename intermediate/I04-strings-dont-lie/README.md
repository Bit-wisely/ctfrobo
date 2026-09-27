I04 - STRINGS DON'T LIE

Points: 10
Category: Intermediate / Binary Analysis  

Challenge Overview  
Compiled executables and binary blobs often contain plain human-readable strings embedded within data sections (`.rodata`, `.data`, `.rdata`). Extracting printable strings from unknown binaries is the first step of basic static analysis before launching a debugger or decompiler.

Participant Question  
Don't execute it. Ask it what words it remembers.

Clue  
Use the standard Linux `strings` utility to print printable character sequences contained inside the binary.

Challenge Files  
- `challenge/mystery.bin`
- `challenge/mystery.c`

Flag Format  
`flag{...}`
