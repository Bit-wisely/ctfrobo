# Solution: B09 - FIND THE PROCESS

Concept
Linux process table inspection, identifying parent-child process relationships (PID/PPID), and recognizing abnormal binary locations.

Walkthrough
1. Examine the process list in processes.txt.
2. Locate the user interactive shell with PID 744.
3. Inspect all child processes spawned by PID 744 (PPID = 744).
4. Notice that /tmp/cache-service is running from the temporary directory /tmp instead of standard system paths like /usr/bin or /usr/sbin.
5. Identify the Process ID (PID) of this rogue process: 1704.

Flag
1704
