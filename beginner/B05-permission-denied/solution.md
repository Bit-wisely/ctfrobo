# Solution: B05 - PERMISSION DENIED

## Concept
The principle of least privilege requires that private credentials and encryption keys be inaccessible to non-privileged users. In Unix/Linux, mode `0600` (`-rw-------`) grants read and write access strictly to the file owner, which is mandatory for secure services like OpenSSH (`chmod 600 id_rsa`).

## Walkthrough
1. Run the validator tool in `challenge/`:
   ```bash
   python3 challenge/verify_access.py
   ```
2. The program outputs:
   ```
   [-] PERMISSION DENIED: Security audit failure!
   [-] Policy requirement: Exactly mode 0600 (Owner Read/Write ONLY: -rw-------).
   ```
3. Inspect current file attributes:
   ```bash
   ls -l challenge/confidential_token.key
   ```
   Output indicates mode `0644` (`-rw-r--r--`).
4. Modify the permissions using `chmod`:
   ```bash
   chmod 600 challenge/confidential_token.key
   ```
5. Rerun the verification tool:
   ```bash
   python3 challenge/verify_access.py
   ```
6. The validator verifies the `0600` mode and decrypts the flag:
   ```
   [+] Vault Flag: permit_least_privilege_600
   ```

## Flag
`permit_least_privilege_600`
