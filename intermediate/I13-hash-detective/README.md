I13 - HASH DETECTIVE

Points: 10
Category: Intermediate / Cryptography & Hashes  

Challenge Overview  
Cryptographic hash functions are one-way mathematical algorithms that transform arbitrary inputs into fixed-length digest outputs (pre-image resistance). When password hashes are recovered from security breaches, analysts perform dictionary attacks using wordlists to identify passwords matching the known hashes.

Participant Question  
You found a fingerprint. You need the word that created it. Everything you need is already here.

Clue  
The target hash is a 32-character hexadecimal string representing an MD5 digest. Hash each word in `wordlist.txt` locally to find the match.

Challenge Files  
- `challenge/hash.txt`
- `challenge/wordlist.txt`

Flag Format  
`flag{<CRACKED_WORD>_password_cracked}`
