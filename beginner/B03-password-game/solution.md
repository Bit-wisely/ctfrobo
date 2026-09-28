Solution: B03 - THE PASSWORD GAME

Concept
Deducing input logic from sample patterns and decoding resulting hexadecimal byte streams.

Walkthrough
1. Run the password program to observe the sample mappings.
2. The examples map each number to its character count (digit length).
3. The prompt 54321 contains 5 digits, so enter 5.
4. The program grants access and outputs hexadecimal bytes: 77656c636f6d6520746f20435446.
5. Use the provided hex-to-ascii converter to decode the hexadecimal string into ASCII text.
6. The decoded string is welcome to CTF.

Flag
welcome to CTF
