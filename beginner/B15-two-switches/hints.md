# Hints: B15 - TWO SWITCHES

### Hint 1
Study the logic state table at the top of the switch card. The output evaluates to true (1) only when the two inputs hold differing binary values.

### Hint 2
Exclusive-OR (XOR) logic is symmetric and self-inverting: applying the exact same key to the ciphertext reverses the transformation without requiring a different decryption algorithm.

### Hint 3
Perform a bitwise XOR operation between each decimal integer value and the provided key (66), then map the resulting numeric values to ASCII characters.
