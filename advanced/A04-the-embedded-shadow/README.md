A04 - THE EMBEDDED SHADOW

Points: 20
Category: Advanced / Steganography

Scenario
An insider threat exfiltrated sensitive data before departing the research facility. Digital forensic investigators recovered an image file (evidence.jpg) alongside an investigator's case notes (case_notes.txt). The suspect utilized cryptographic steganography (steghide) to conceal an encrypted payload within the image.

Objective
Analyze the recovered investigative notes to discover the extraction parameters and passphrase. Use steghide (or the included extraction utility) to extract the secret payload from evidence.jpg and uncover the flag.

Execution Reference
To run Python files: python filename.py
To compile and run C files: gcc filename.c -o output && ./output
Linux Steghide Command: steghide extract -sf evidence.jpg -p <passphrase>
