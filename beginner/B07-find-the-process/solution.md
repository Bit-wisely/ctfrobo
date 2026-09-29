# Solution: B07 - FIND THE PROCESS

## Concept
Linux process management links child processes to their parent via Parent Process IDs (PPID). System programs typically execute from standard system paths (`/usr/bin`, `/sbin`), whereas unauthorized or transient binaries frequently run from writable scratch directories such as `/tmp`.

## Walkthrough
1. Inspect the process list in `challenge/processes.txt`.
2. Locate the user's interactive shell session:
   ```
   user       744     731     0.1    0.7    S       -bash
   ```
3. Inspect the child processes spawned by shell session `PID 744` (records where `PPID = 744`).
4. Notice process `1704`:
   ```
   user      1704     744     0.2    0.4    S       /tmp/cache-service
   ```
5. Unlike standard user binaries located in `/usr/bin/`, `/tmp/cache-service` executes from `/tmp`.
6. The Process ID (PID) is `1704`.

## Flag
`1704`
