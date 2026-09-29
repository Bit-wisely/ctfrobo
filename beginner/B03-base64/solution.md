Solution: B03 - BASE64 ISN'T ENCRYPTION

Concept
Base64 encoding/decoding and recognizing standard data representations versus true cryptography.

Walkthrough
1. Inspect the encoded text in `challenge/message.txt`:
   ```text
   YmFzZTY0
   ```
2. Decode the string using command-line tools:
   ```bash
   echo "YmFzZTY0" | base64 -d
   ```
   Or run the included interactive Python script:
   ```bash
   python challenge/converter.py
   ```
   and select option 1 to decode `YmFzZTY0`.
3. The decoded output yields: `base64`.

Flag
base64
