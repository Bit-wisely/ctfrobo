# Solution: B03 - BASE64 ISN'T ENCRYPTION

## Concept
Base64 representation maps binary octets into 6-bit values represented by an ASCII charset (A-Z, a-z, 0-9, +, /) with `=` used as trailing padding. Because it requires no secret key, Base64 is an encoding format, not encryption.

## Walkthrough
1. Inspect the encoded text in `challenge/message.txt`:
   ```
   cHJvdG9jb2xfc3RyZWFtX2VjaG9fMjQ=
   ```
2. Identify the character set and padding as standard Base64 representation.
3. Decode the string using standard terminal utilities:
   ```bash
   echo "cHJvdG9jb2xfc3RyZWFtX2VjaG9fMjQ=" | base64 -d
   ```
4. The decoded plaintext revealed is:
   ```
   protocol_stream_echo_24
   ```

## Flag
`protocol_stream_echo_24`
