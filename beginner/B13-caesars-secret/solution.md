# Solution: B13 - CAESAR'S SECRET

## Concept
The Caesar cipher displaces every letter in the alphabet by a fixed integer key $k \pmod{26}$. In sufficiently long English texts, statistical frequency analysis reveals that 'E' is the most frequent character. Finding the shift difference between the most frequent ciphertext letter and 'E' reveals the secret shift key.

## Walkthrough
1. Inspect `challenge/message.txt` and perform a letter frequency count:
   ```python
   from collections import Counter
   with open("challenge/message.txt") as f:
       text = f.read()
   counts = Counter(c for c in text if c.isalpha())
   print(counts.most_common(5))
   ```
2. The letter `L` is the most common with 94 occurrences, followed by `A` with 75.
3. Compare the peak frequency against the standard English peak 'E':
   - Distance from 'E' (ordinal 4) to 'L' (ordinal 11) is $11 - 4 = +7$.
   - Common three-letter word `AOL` shifted backward by 7 produces `THE`.
4. Decrypt the message using a shift of $-7$ (or $+19$):
   ```python
   def decrypt(text, s=7):
       res = []
       for c in text:
           if 'A' <= c <= 'Z':
               res.append(chr((ord(c) - ord('A') - s) % 26 + ord('A')))
           elif 'a' <= c <= 'z':
               res.append(chr((ord(c) - ord('a') - s) % 26 + ord('a')))
           else:
               res.append(c)
       return "".join(res)
   ```
5. Decrypted message reads:
   ```
   THE IMPERIAL TACTICAL DISPATCH AND ENCRYPTED FIELD REPORT.
   ...
   THE CONFIDENTIAL PASSCODE REQUIRED TO AUTHENTICATE COMMAND HEADQUARTERS IS CENTURION_SHIELD_42.
   ```
6. The recovered uppercase flag is:
   ```
   CENTURION_SHIELD_42
   ```

## Flag
`CENTURION_SHIELD_42`
