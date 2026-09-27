**A10 - COMMAND INJECTION**

**Points**: 450  
**Category**: Advanced / Command Injection  

**Challenge Overview**  
Command Injection vulnerabilities occur when an application passes unsanitized user-supplied data to a system shell execution function (`system()`, `popen()`, `subprocess.Popen(shell=True)`). Attackers utilize shell metacharacters (such as `;`, `&&`, `|`) to execute arbitrary operating system commands with the privileges of the web application.

**Participant Question**  
The application needs to run a command. It asks you for an argument. How much control does that argument really give you?

**Clue**  
Chain commands together using shell metacharacters like `;` or `&&` (e.g. `127.0.0.1; cat flag.txt`) to execute unauthorized operating system commands.

**Challenge Files**  
- `challenge/app/app.py`
- `challenge/app/flag.txt`

**Flag Format**  
`flag{...}`
