Hints: A01 - THE BINARY SECRET

1. The validation logic transforms input bytes using `input[i] ^ 0x37`.
2. Decoy strings in `strings` output are distractors; analyze the array comparisons.
3. Compute `expected[i] ^ 0x37` for every byte in the array to reconstruct the flag.
