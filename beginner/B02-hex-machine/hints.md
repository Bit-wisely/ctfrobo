# Hints: B02 - HEX MACHINE

### Hint 1
Examine the output stream. Every element is a two-character token drawn from the numerals `0-9` and lowercase letters `a-f`.

### Hint 2
Each two-digit token represents an 8-bit value expressed in radix 16 (hexadecimal notation). In computing, hexadecimal pairs directly represent raw memory bytes and characters.

### Hint 3
Use the Hexadecimal to ASCII reference table below to map the hexadecimal pairs to their corresponding characters:

#### Hexadecimal to ASCII Reference Table
| Hex | ASCII | Hex | ASCII | Hex | ASCII | Hex | ASCII |
|:---:|:-----:|:---:|:-----:|:---:|:-----:|:---:|:-----:|
| 20  | Space | 61  |   a   | 6e  |   n   | 30  |   0   |
| 5f  |   _   | 62  |   b   | 6f  |   o   | 31  |   1   |
| 2d  |   -   | 63  |   c   | 70  |   p   | 32  |   2   |
| 2e  |   .   | 64  |   d   | 71  |   q   | 33  |   3   |
| 41  |   A   | 65  |   e   | 72  |   r   | 34  |   4   |
| 42  |   B   | 66  |   f   | 73  |   s   | 35  |   5   |
| 43  |   C   | 67  |   g   | 74  |   t   | 36  |   6   |
| 44  |   D   | 68  |   h   | 75  |   u   | 37  |   7   |
| 45  |   E   | 69  |   i   | 76  |   v   | 38  |   8   |
| 46  |   F   | 6a  |   j   | 77  |   w   | 39  |   9   |
| 47  |   G   | 6b  |   k   | 78  |   x   |     |       |
| 48  |   H   | 6c  |   l   | 79  |   y   |     |       |
| 49  |   I   | 6d  |   m   | 7a  |   z   |     |       |
