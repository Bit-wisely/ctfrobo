A04 - THE EMBEDDED SHADOW

Points: 20
Category: Advanced / Steganography

Scenario
An insider threat exfiltrated sensitive data before departing the research facility. Digital forensic investigators recovered an image file (evidence.jpg) alongside an investigator's triage case notes (case_notes.txt). The suspect utilized cryptographic steganography (`steghide`) to conceal an encrypted payload within the image's discrete cosine transform (DCT) coefficients.

Objective
1. Analyze the recovered investigative case notes (`case_notes.txt`) to identify and recover the extraction passphrase.
2. Use `steghide` (or the included extraction utility) to extract the concealed dossier (`secret.txt`) from `evidence.jpg`.
3. Analyze and decode the extracted transmission block inside `secret.txt` to uncover the final flag.

Command Syntax Reference
- Linux Steghide Extraction Command:
  ```bash
  steghide extract -sf evidence.jpg -p <passphrase>
  ```

- Inspect Extracted Dossier:
  ```bash
  cat secret.txt
  ```
