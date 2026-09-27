**B13 - TWO SWITCHES**

**Points**: 250  
**Category**: Beginner / Cryptography & Bitwise Logic  

**Challenge Overview**  
The Exclusive OR (XOR) operation is ubiquitous in modern cryptography, stream ciphers, and one-time pads. When two identical bits are XORed, the result is 0; when different, the result is 1. Crucially, XOR is completely reversible using the same key: `(Plaintext ^ Key) ^ Key = Plaintext`.

**Participant Question**  
Two switches control one light. When both are off, the light is off. When both are on, the light is also off. But when exactly one is on, the light changes. Follow the switches and find the message.

**Clue**  
The truth table describes the XOR bitwise operation. XOR each number in `switches.txt` with key 66 to reverse the cipher.

**Challenge Files**  
- `challenge/switches.txt`

**Flag Format**  
`flag{...}`
