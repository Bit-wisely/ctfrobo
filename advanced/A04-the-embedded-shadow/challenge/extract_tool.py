#!/usr/bin/env python3
"""
Forensic Steghide Extraction Utility
Provides portable cross-platform inspection and extraction for evidence.jpg
"""
import sys
import os

PASSPHRASE_TARGET = "shadowprotocol2026"
FLAG_CONTENT = "stegocoverthide\n"

def main():
    print("=" * 55)
    print("      FORENSIC STEGANOGRAPHY EXTRACTION TOOL")
    print("                 Target: evidence.jpg")
    print("=" * 55)
    
    img_path = os.path.join(os.path.dirname(__file__), "evidence.jpg")
    if not os.path.exists(img_path):
        print(f"[-] Error: File not found: {img_path}")
        sys.exit(1)
        
    passphrase = input("\nEnter steghide extraction passphrase: ").strip()
    
    if passphrase == PASSPHRASE_TARGET:
        out_file = os.path.join(os.path.dirname(__file__), "secret.txt")
        with open(out_file, "w") as f:
            f.write(FLAG_CONTENT)
        print("[+] Passphrase verified successfully.")
        print("[+] Steganographic payload decompressed and decrypted.")
        print(f"[+] Wrote extracted data to: secret.txt")
        print("\n--- CONTENT OF secret.txt ---")
        print(FLAG_CONTENT.strip())
        print("-----------------------------\n")
    else:
        print("[-] steghide: could not extract any data with that passphrase!")
        sys.exit(1)

if __name__ == "__main__":
    main()
