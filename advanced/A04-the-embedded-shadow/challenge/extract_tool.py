#!/usr/bin/env python3
"""
Forensic Steghide Extraction Utility
Provides portable cross-platform inspection and extraction for evidence.jpg
"""
import sys
import os

PASSPHRASE_TARGET = "locked"
FLAG_CONTENT = """================================================================================
           CLASSIFIED SHADOW PROTOCOL - EXFILTRATION DOSSIER
================================================================================
SECURITY CLEARANCE : LEVEL 5 (TOP SECRET // EYES ONLY)
TARGET ASSET       : DCT TRANSFORM COEFFICIENTS
STATUS             : EXTRACTED VIA STEGANOGRAPHIC RECOVERY
================================================================================

[+] Carrier payload successfully recovered from evidence image.
[-] NOTICE: To prevent unauthorized inspection upon extraction, the primary
    intelligence flag has been secured through a two-stage cryptographic pipeline:

    STAGE 1: Bitwise XOR Masking using Key: "PIXEL"
    STAGE 2: Standard Base64 ASCII Armor

[ENCODED TRANSMISSION BLOCK]:
--------------------------------------------------------------------------------
OT0HLD8PJDc3KQ89MCQiDzkxPSk8
--------------------------------------------------------------------------------

[FORENSIC DECRYPTION INSTRUCTIONS]:
Reverse the exfiltration pipeline to uncover the flag:
1. Base64 decode the transmission block into raw bytes.
2. Apply bitwise XOR against the repetitive ASCII key: "PIXEL"

Example Python one-liner:
python3 -c "import base64; k=b'PIXEL'; b=base64.b64decode('OT0HLD8PJDc3KQ89MCQiDzkxPSk8'); print(''.join(chr(c^k[i%len(k)]) for i,c in enumerate(b)))"
================================================================================
"""

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
    
    if passphrase.lower() == PASSPHRASE_TARGET:
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
