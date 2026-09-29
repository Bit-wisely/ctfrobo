Solution: A04 - THE EMBEDDED SHADOW

Concept
Cryptographic steganography in JPEG images using `steghide`, passphrase recovery from forensic case notes, and embedded payload extraction.

Walkthrough
1. Inspect `challenge/case_notes.txt`:
   ```text
   Passphrase policy: shadowprotocol2026
   ```
2. Note that the suspect used `steghide` on `evidence.jpg`.
3. Extract the secret payload using `steghide` in terminal:
   ```bash
   steghide extract -sf challenge/evidence.jpg -p shadowprotocol2026
   ```
   *Or* run the interactive forensic utility:
   ```bash
   python challenge/extract_tool.py
   ```
   and enter the passphrase `shadowprotocol2026`.
4. The extraction outputs `secret.txt` containing:
   ```text
   stegocoverthide
   ```
5. Flag is retrieved: `stegocoverthide`.

Flag
stegocoverthide
