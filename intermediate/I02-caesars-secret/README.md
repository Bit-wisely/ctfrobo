I02 - CAESAR'S SECRET

Points: 10
Category: Intermediate / Classical Cryptography  

Challenge Overview  
The Caesar cipher is one of the earliest known encryption techniques. It operates as a monoalphabetic substitution cipher where each letter in the plaintext is shifted by a fixed number of positions down the alphabet. In CTF competitions, recognizing shifted flag formats (`IODJ{...}` matching `FLAG{...}`) allows instant cryptanalysis.

Participant Question  
Someone decided that shifting letters was enough to keep a secret. Recover the message.

Clue  
Compare the encrypted prefix `IODJ` with the known flag prefix `FLAG`. Determine the alphabet shift amount and shift each letter backward.

Challenge Files  
- `challenge/message.txt`

Flag Format  
`flag{...}`
