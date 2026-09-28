Solution: I13 - HASH DETECTIVE

Concept  
MD5 cryptographic hashing and offline dictionary attacks.

Walkthrough  
1. Inspect `challenge/hash.txt`:
   `42a03cf0a6cf3be9a2ea9c98a58402ee`
2. Test candidate passwords in `challenge/wordlist.txt` against MD5:
   ```python
   import hashlib
   print(hashlib.md5(b"shadow").hexdigest())
   ```
3. `shadow` matches the hash digest.
4. Format the flag: `flag{shadow password cracked}`.

Flag  
`flag{shadow password cracked}`
