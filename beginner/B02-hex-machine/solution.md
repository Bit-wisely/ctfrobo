# Solution: B02 - HEX MACHINE

## Concept
Hexadecimal (base-16) uses symbols 0-9 and a-f to represent 4 bits (a nibble). A pair of hex digits represents 8 bits (one full byte), which can map directly to ASCII characters.

## Walkthrough
1. Run the script or inspect the tokens:
   ```
   6d 61 74 72 69 78 5f 62 65 61 63 6f 6e 5f 6f 6e 6c 69 6e 65 5f 38 38
   ```
2. Convert each hex pair to its ASCII character representation:
   - `6d` -> 'm'
   - `61` -> 'a'
   - `74` -> 't'
   - `72` -> 'r'
   - `69` -> 'i'
   - `78` -> 'x'
   - `5f` -> '_'
   - `62` -> 'b'
   - `65` -> 'e'
   - `61` -> 'a'
   - `63` -> 'c'
   - `6f` -> 'o'
   - `6e` -> 'n'
   - `5f` -> '_'
   - `6f` -> 'o'
   - `6e` -> 'n'
   - `6c` -> 'l'
   - `69` -> 'i'
   - `6e` -> 'n'
   - `65` -> 'e'
   - `5f` -> '_'
   - `38` -> '8'
   - `38` -> '8'
3. Assemble the characters:
   ```
   matrix_beacon_online_88
   ```

## Flag
`matrix_beacon_online_88`
