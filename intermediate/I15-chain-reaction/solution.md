Solution: I15 - CHAIN REACTION

Concept  
Multi-stage forensic workflows combining Base64 decoding, hidden files, and hex decoding.

Walkthrough  
1. Decode Base64 in `challenge/mystery.bin`:
   `Y2hhbGxlbmdlL2FyY2hpdmUvLnNlY3JldF9jbHVl` -> `challenge/archive/.secret_clue`
2. Open `challenge/archive/.secret_clue` to read the hex string:
   `6d756c746920737461676520666f72656e7369637320736f6c766564`
3. Decode hex bytes to ASCII:
   `multi stage forensics solved`

Flag  
`multi stage forensics solved`
