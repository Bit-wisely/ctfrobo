# Architecture and Design

The question bank is organized into three balanced tiers of difficulty consisting of 31 curated cybersecurity CTF challenges:

---

### Beginner Tier (B01 - B15) — 5 Points Each (75 pts total)

Focuses on foundational cybersecurity, data representation, and Linux/network literacy:
- **B01:** Base64 representation and decoding
- **B02:** Hexadecimal to ASCII decoding
- **B03:** Binary to ASCII decoding
- **B04:** Linux hidden files and directory discovery (`ls -la`)
- **B05:** Linux file system permissions (`chmod`, `ls -l`)
- **B06:** Log investigation and pattern filtering (`grep`)
- **B07:** Process management and identification (`ps`, `top`)
- **B08:** Standard TCP port reconnaissance (HTTP vs. HTTPS)
- **B09:** IPv4 subnets, CIDR notation, and network addressing
- **B10:** Client-side HTML source comment inspection & recon
- **B11:** File signature detection, magic bytes, and archive extraction
- **B12:** Phishing email analysis and header forensics
- **B13:** Classical rotational substitution (Caesar cipher)
- **B14:** Relational database querying and SQL inspection
- **B15:** Bitwise XOR operations and reversible encryption

---

### Intermediate Tier (I01 - I08) — 10 Points Each (80 pts total)

Focuses on security tooling, forensic analysis, steganography, and web security:
- **I01:** Magic byte repair and corrupted file signature restoration
- **I02:** EXIF metadata analysis and hidden image attributes
- **I03:** Least Significant Bit (LSB) image pixel steganography
- **I04:** Packet capture (PCAP) inspection and traffic stream analysis
- **I05:** Session cookie decoding and privilege tampering
- **I06:** DNS query log threat hunting and malicious C2 domain identification
- **I07:** Cryptographic hash identification and dictionary/rainbow cracking
- **I08:** Multi-stage forensic investigation workflow

---

### Advanced Tier (A01 - A08) — 20 Points Each (160 pts total)

Focuses on binary reverse engineering, exploitation, covert exfiltration, and high-impact web vulnerabilities:
- **A01:** ELF binary disassembly and control flow reverse engineering
- **A02:** Hidden backdoor logic and undocumented trigger discovery in compiled binaries
- **A03:** Parser vulnerability exploitation and sandbox/jailbreak escape
- **A04:** Cryptographic steganography inside JPEG images using `steghide`
- **A05:** In-depth multi-stream PCAP dissection and payload carving
- **A06:** Covert data exfiltration detection through DNS tunneling
- **A07:** Dynamic SQL injection authentication bypass and database extraction
- **A08:** Remote Code Execution (RCE) via operating system command injection
