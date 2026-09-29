Solution: A04 - THE EMBEDDED SHADOW

Concept
Cryptographic steganography in JPEG images using `steghide`, forensic passphrase recovery from triage memory artifacts, and multi-stage payload de-obfuscation (Base64 + bitwise XOR).

Walkthrough
1. Inspect `challenge/case_notes.txt`:
   The investigator recovered a configuration fragment containing:
   ```text
   PASS_HEX: 6c6f636b6564
   HASH_SHA256: 14493f5f5470ed48c3f103d917ec52ae9005fa3913128031d0fac2a49ac3cc41
   PASS_HINT: Status of a secured facility vault (6 lowercase letters).
   ```
2. Convert the hexadecimal string `6c6f636b6564` to ASCII:
   ```bash
   python3 -c "print(bytes.fromhex('6c6f636b6564').decode())"
   ```
   Output: `locked`

3. Extract the secret payload from `evidence.jpg` using `steghide`:
   ```bash
   steghide extract -sf challenge/evidence.jpg -p locked
   ```
   *Or* run the interactive forensic utility:
   ```bash
   python challenge/extract_tool.py
   ```
   and enter the passphrase `locked`.

4. The extraction produces `secret.txt` containing an exfiltration dossier:
   ```text
   STAGE 1: Bitwise XOR Masking using Key: "PIXEL"
   STAGE 2: Standard Base64 ASCII Armor

   [ENCODED TRANSMISSION BLOCK]:
   OT0HLD8PJDc3KQ89MCQiDzkxPSk8
   ```

5. Reverse the two-stage cryptographic pipeline:
   - Base64-decode `OT0HLD8PJDc3KQ89MCQiDzkxPSk8`.
   - XOR each byte with repeating key `PIXEL`.
   ```bash
   python3 -c "import base64; k=b'PIXEL'; b=base64.b64decode('OT0HLD8PJDc3KQ89MCQiDzkxPSk8'); print(''.join(chr(c^k[i%len(k)]) for i,c in enumerate(b)))"
   ```
   Output: `it_is_more_than_pixel`

Flag
it_is_more_than_pixel
