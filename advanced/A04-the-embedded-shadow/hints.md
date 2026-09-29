Hints: A04 - THE EMBEDDED SHADOW

1. Inspect case_notes.txt to identify which steganography software and configuration passphrase the suspect used.
2. Standard image metadata viewers like exiftool will not reveal the hidden file because steghide encrypts and embeds data inside the DCT transform coefficients of JPEG images.
3. Use the command `steghide extract -sf evidence.jpg -p <passphrase>` on Ubuntu, or run the provided Python forensic tool `extract_tool.py` to extract the embedded file.
