Hints: I13 - HASH DETECTIVE

1. A 32-character hexadecimal digest matches the 128-bit output of MD5.
2. Iterate through each entry in `challenge/wordlist.txt` and compute `hashlib.md5(w.encode()).hexdigest()`.
3. The matching plaintext word is `shadow`.
