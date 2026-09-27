**I01 - BASE64 ISN'T ENCRYPTION**

**Points**: 250  
**Category**: Intermediate / Encodings  

**Challenge Overview**  
Base64 is a binary-to-text encoding scheme designed to represent binary data in an ASCII string format by translating it into a radix-64 representation. A common misconception among beginners is conflating data encoding with cryptographic encryption. Because Base64 uses no key and has no confidentiality guarantees, anyone can instantaneously decode it.

**Participant Question**  
Someone left a message. It looks like random letters and numbers. They claim it is protected. Find out what they actually did.

**Clue**  
Look for standard Base64 characters and character set patterns. Use the `base64 -d` utility to decode the payload.

**Challenge Files**  
- `challenge/message.txt`

**Flag Format**  
`flag{...}`
