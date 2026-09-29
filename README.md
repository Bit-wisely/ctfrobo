# Cybersecurity CTF Question Bank

A structured, beginner-to-advanced Cybersecurity Capture The Flag challenge repository.

## Scoring Rules
- **Beginner Track (15 Challenges):** 5 points each (75 points total)
- **Intermediate Track (8 Challenges):** 10 points each (80 points total)
- **Advanced Track (8 Challenges):** 20 points each (160 points total)
- **Total Event Score:** 315 points across 31 curated challenges

## Workstation Prerequisites & Software Policy
- Standard Linux / Ubuntu environment (or offline CTF participant VM)
- Standard core tools: Python 3 (`python3`), GCC (`gcc`), and standard terminal utilities (`grep`, `strings`, `base64`, `file`)
- **Third-Party Software Policy:** **Only `steghide` is allowed as third-party software** (required for Advanced challenge A04: `sudo apt install -y steghide`). No other external tools are permitted or needed.
- All network and PCAP investigations are performed using native Python scripts and standard utilities provided within the challenge packages.

## Question Format
All challenges contain standardized README descriptions, hint guides, solutions, and challenge distribution packages.

---

## Challenge Tracks

### Beginner Track (5 Points Each — 15 Challenges)
- **B01:** THE MACHINE SPEAKS (Binary to ASCII)
- **B02:** HEX MACHINE (Hexadecimal to ASCII)
- **B03:** BASE64 ISN'T ENCRYPTION (Base64 Encoding & Representation)
- **B04:** HIDDEN IN PLAIN SIGHT (Linux / Filesystem Navigation)
- **B05:** PERMISSION DENIED (Linux / File Permissions)
- **B06:** READ BETWEEN THE LINES (Linux / Text Investigation & grep)
- **B07:** FIND THE PROCESS (Linux Administration / Process Management)
- **B08:** WHICH DOOR? (Network Ports & Services)
- **B09:** FIND THE SERVER (IPv4 Network Subnets)
- **B10:** THE SOURCE KNOWS (Web Reconnaissance / HTML Source Comments)
- **B11:** THE WRONG FILE (Linux / File Signatures & Archives)
- **B12:** THE INBOX TRAP (Phishing / Email Forensics)
- **B13:** CAESAR'S SECRET (Classical Cryptography / Shift Cipher)
- **B14:** THE DATABASE KNOWS (SQL Database Queries)
- **B15:** TWO SWITCHES (Cryptography / Bitwise XOR)

---

### Intermediate Track (10 Points Each — 8 Challenges)
- **I01:** THE FILE THAT PRETENDS (Forensics / File Signatures & Magic Bytes)
- **I02:** THE PHOTOGRAPH REMEMBERS (Forensics / EXIF Metadata Analysis)
- **I03:** SMALLEST BITS (Steganography / LSB Image Stego)
- **I04:** THE CAPTURED CONVERSATION (Network Forensics / Packet Inspection)
- **I05:** COOKIE TROUBLE (Web Security / Cookie & Session Tampering)
- **I06:** DNS DETECTIVE (Threat Hunting / DNS Log Analysis)
- **I07:** HASH DETECTIVE (Cryptography / Hash Identification & Cracking)
- **I08:** CHAIN REACTION (Multi-Stage Forensics)

---

### Advanced Track (20 Points Each — 8 Challenges)
- **A01:** THE BINARY SECRET (Reverse Engineering / Binary Disassembly)
- **A02:** THE PROGRAM HAS A BACKDOOR (Reverse Engineering / Hidden Logic Analysis)
- **A03:** JAILBREAK THE BOX (Exploitation / Parser Sandbox Escape)
- **A04:** THE EMBEDDED SHADOW (Advanced Steganography / steghide)
- **A05:** PCAP INVESTIGATION (Deep Packet Forensics & Stream Carving)
- **A06:** DNS EXFILTRATION (Threat Analysis / Covert DNS Tunneling)
- **A07:** SQL INJECTION (Web Exploitation / Dynamic SQLi)
- **A08:** COMMAND INJECTION (Web Exploitation / Remote Code Execution)
