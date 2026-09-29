# Hints: B07 - FIND THE PROCESS

### Hint 1
Rather than focusing solely on Process IDs, analyze the relational columns that describe who invoked each program and what command was executed.

### Hint 2
Distinguish between system-level services spawned by the init system (PPID 1) and child tasks spawned interactively under active user login sessions.

### Hint 3
Examine the filesystem locations of the binaries. Standard Unix utilities reside in structured paths like `/usr/bin` or `/usr/sbin`, whereas unauthorized programs frequently run from temporary directories like `/tmp`.
