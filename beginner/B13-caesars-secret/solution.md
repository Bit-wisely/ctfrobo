# Solution: B13 - CAESAR'S SECRET

## Concept
The Caesar cipher is a monoalphabetic substitution cipher where each character in the plaintext is shifted by a fixed key $k$ positions down the alphabet ($c = (p + k) \pmod{26}$).

## Walkthrough
1. Inspect `challenge/message.txt`:
   ```
   FHQWXULRQ_VKLHOG_42
   ```
2. Test rotational shifts using `challenge/converter.py` or a Caesar brute-force loop.
3. Rotating backward by 3 positions (or +23 modulo 26):
   - `F` (-3) -> 'c'
   - `H` (-3) -> 'e'
   - `Q` (-3) -> 'n'
   - `W` (-3) -> 't'
   - `X` (-3) -> 'u'
   - `U` (-3) -> 'r'
   - `L` (-3) -> 'i'
   - `R` (-3) -> 'o'
   - `Q` (-3) -> 'n'
   - `_` -> '_'
   - `V` (-3) -> 's'
   - `K` (-3) -> 'h'
   - `L` (-3) -> 'i'
   - `H` (-3) -> 'e'
   - `O` (-3) -> 'l'
   - `G` (-3) -> 'd'
   - `_` -> '_'
   - `4` -> '4'
   - `2` -> '2'
4. The decoded plaintext is:
   ```
   centurion_shield_42
   ```

## Flag
`centurion_shield_42`
