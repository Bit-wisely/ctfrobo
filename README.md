Cybersecurity CTF - Complete Question Bank

A structured collection of Capture The Flag (CTF) challenges categorized into Beginner, Intermediate, and Advanced tiers.

---

Repository Structure

```text
cybersecurity-ctf/
├── README.md
├── documentation/
│   ├── architecture.md
│   ├── rules.md
│   └── scoring.md
├── beginner/
│   ├── B01-machine-speaks/
│   ├── B02-hex-machine/
│   ├── B03-last-one-out/
│   ├── B04-file-that-isnt-there/
│   ├── B05-follow-the-loop/
│   ├── B06-pointers-secret/
│   ├── B07-the-searcher/
│   ├── B08-find-the-process/
│   ├── B09-which-door/
│   ├── B10-find-the-server/
│   ├── B11-the-database-knows/
│   ├── B12-the-numbers-lie/
│   ├── B13-two-switches/
│   ├── B14-missing-character/
│   └── B15-the-chain/
├── intermediate/
│   ├── I01-base64/
│   ├── I02-caesars-secret/
│   ├── I03-file-that-pretends/
│   ├── I04-strings-dont-lie/
│   ├── I05-photograph-remembers/
│   ├── I06-smallest-bits/
│   ├── I07-captured-conversation/
│   ├── I08-cookie-trouble/
│   ├── I09-source-knows/
│   ├── I10-robots-know/
│   ├── I11-headers-speak/
│   ├── I12-dns-detective/
│   ├── I13-hash-detective/
│   ├── I14-sql-question/
│   └── I15-chain-reaction/
└── advanced/
    ├── A01-binary-secret/
    ├── A02-program-has-a-backdoor/
    ├── A03-jailbreak-the-box/
    ├── A04-stego-chain/
    ├── A05-pcap-investigation/
    ├── A06-dns-exfiltration/
    ├── A07-cookie-forgery/
    ├── A08-sql-injection/
    ├── A09-blind-sql/
    ├── A10-command-injection/
    ├── A11-path-traversal/
    ├── A12-jwt/
    ├── A13-broken-authentication/
    └── A14-web-chain/
```

---

Standard Challenge Format

Every challenge directory contains:
- README.md: Problem statement, challenge overview, clear clue description, and metadata.
- challenge/: Distribution files and artifacts given to participants.
- hints.md: Progressive guidance.
- solution.md: Complete technical walkthrough and concept breakdown.
- answer.txt: Exact flag value.

---

Scoring Summary

| Tier | Challenge Range | Points per Challenge |
| :--- | :--- | :--- |
| Beginner | B01 - B15 | 5 |
| Intermediate | I01 - I15 | 10 |
| Advanced | A01 - A14 | 20 |

