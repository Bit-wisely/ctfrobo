A02 - THE PROGRAM HAS A BACKDOOR

Points: 20
Category: Advanced / Reverse Engineering  

Challenge Overview  
Command-line interfaces and firmware shells often contain undocumented administrative commands left behind by developers for debugging or diagnostic testing. In security assessments, analyzing the full command parsing table exposes hidden backdoor functions.

Participant Question  
The program has a normal interface. Or at least, that's what it wants you to believe. Someone left another way in.

Clue  
Inspect the command dispatch logic in `program.c` to find undocumented commands not listed in the help menu.

Challenge Files  
- `challenge/program.c`
- `challenge/program.py`

Flag Format  
`flag{...}`
