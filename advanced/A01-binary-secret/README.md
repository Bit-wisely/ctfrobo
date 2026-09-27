A01 - THE BINARY SECRET

Points: 20
Category: Advanced / Reverse Engineering  

Challenge Overview  
Software protection mechanisms frequently obfuscate comparison logic to prevent reverse engineers from discovering passwords through static strings alone. When a program transforms your input byte-by-byte before checking against an internal array, reversing that transformation algorithm reveals the valid input.

Participant Question  
The program knows the answer. It just doesn't want to tell you. You don't have the source code. Find out what the program is checking.

Clue  
The program applies an XOR operation with key `0x37` to each input character and compares the result against a hardcoded byte array. Reverse the XOR transformation on the byte constants.

Challenge Files  
- `challenge/mystery.c`
- `challenge/mystery.py`

Flag Format  
`flag{...}`
