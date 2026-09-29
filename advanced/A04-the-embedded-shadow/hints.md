Hints: A04 - THE EMBEDDED SHADOW

1. Inspect `case_notes.txt`: The suspect's memory config fragment contains `PASS_HEX: 6c6f636b6564`. Convert this hex string to ASCII (or match against the SHA-256 hash) to recover the 6-letter passphrase.
2. Standard metadata tools will not reveal the hidden data. Use `steghide extract -sf evidence.jpg -p <passphrase>` on Linux (or run `python extract_tool.py`) to extract `secret.txt`.
3. The extracted `secret.txt` contains an exfiltration dossier. Base64-decode the transmission block and XOR the resulting bytes with the key `PIXEL` to uncover the flag.
