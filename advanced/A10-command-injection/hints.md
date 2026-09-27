**Hints: A10 - COMMAND INJECTION**

1. The `host` query parameter is formatted directly into a system command: `ping -c 1 {host}`.
2. Shell control characters such as `;` allow chaining multiple shell commands.
3. Submit `127.0.0.1; cat flag.txt` to dump the secret flag file.
