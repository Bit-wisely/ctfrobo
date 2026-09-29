Hints: A05 - PCAP INVESTIGATION

1. The flag is not stored as plaintext in the PCAP; naive string searches or simple grep commands will fail.
2. Follow the HTTP C2 stream between 10.0.2.15 and 198.51.100.88 to locate the handshake response containing the XOR decryption key and chunk assembly manifest.
3. Filter for traffic on the custom exfiltration port (port 8888). Reorder the received chunks according to the manifest, parse the hexadecimal bytes, and apply the XOR key.
