# Solution: B04 - HIDDEN IN PLAIN SIGHT

## Concept
In Unix and Linux filesystems, entries prefixed with a dot (`.`) are hidden from standard directory listings (`ls`) unless explicitly queried with the all (`-a` / `-la`) flag.

## Walkthrough
1. Navigate into the challenge directory:
   ```bash
   cd challenge/case
   ```
2. Execute a detailed listing including hidden items:
   ```bash
   ls -la
   ```
3. Observe the hidden directory named `.hidden`:
   ```
   drwxr-xr-x .hidden
   ```
4. Read the file located inside `.hidden`:
   ```bash
   cat .hidden/message.txt
   ```
5. The answer extracted is:
   ```
   dot_entry_unlocked_37
   ```

## Flag
`dot_entry_unlocked_37`
