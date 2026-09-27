A03 - JAILBREAK THE BOX

Points: 20
Category: Advanced / Sandbox Security  

Challenge Overview  
Restricted shells and execution sandboxes aim to limit participant access to a strict whitelist of safe commands. However, custom command parsers that improperly handle argument expansion or special variables can be manipulated into executing forbidden actions.

Participant Question  
Welcome to the box. You have a few commands. The flag is not one of them. But the box was written by a human. Humans make mistakes.

Clue  
The sandbox permits the `echo` command. Test how arguments containing variables like `$FLAG` are parsed.

Challenge Files  
- `challenge/jail.c`
- `challenge/jail.py`

Flag Format  
`flag{...}`
