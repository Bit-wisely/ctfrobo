#!/usr/bin/env python3
import os
import stat
import sys

TOKEN_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "confidential_token.key")

def check_and_unlock():
    print("=== Access Guardian: Security Policy Validator ===")
    
    if not os.path.exists(TOKEN_FILE):
        print(f"[-] Error: Target file '{TOKEN_FILE}' not found.")
        sys.exit(1)
        
    file_stat = os.stat(TOKEN_FILE)
    mode = stat.S_IMODE(file_stat.st_mode)
    octal_mode = oct(mode)[2:].zfill(4)
    
    print(f"[*] Checking file: {os.path.basename(TOKEN_FILE)}")
    print(f"[*] Detected permissions: mode {octal_mode} ({stat.filemode(file_stat.st_mode)})")
    
    if mode != 0o600:
        print("\n[-] PERMISSION DENIED: Security audit failure!")
        print("[-] The credential file has unsafe or non-compliant permissions.")
        print("[-] Policy requirement: Exactly mode 0600 (Owner Read/Write ONLY: -rw-------).")
        print("[-] Others or group must NOT have read, write, or execute rights.")
        print("[!] Adjust file permissions using 'chmod' and rerun the validator.")
        sys.exit(1)
        
    print("\n[+] SUCCESS: Least-privilege permission policy verified (0600).")
    print("[+] File is strictly protected against unauthorized local access.")
    print("[+] Decrypting authorization vault token...\n")
    
    with open(TOKEN_FILE, "r") as f:
        for line in f:
            if line.startswith("CIPHERTEXT:"):
                raw_hex = line.split(":", 1)[1].strip()
                raw_bytes = bytes.fromhex(raw_hex)
                flag = "".join(chr(b ^ 0x5A) for b in raw_bytes)
                print(f"[+] Vault Flag: {flag}")
                return
                
    print("[-] Error: Corrupted token payload.")

if __name__ == "__main__":
    check_and_unlock()
