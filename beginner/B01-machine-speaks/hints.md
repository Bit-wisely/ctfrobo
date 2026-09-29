# Hints: B01 - THE MACHINE SPEAKS

### Hint 1
Look at the raw program output. The data is serialized into lines containing only `0` and `1` characters.

### Hint 2
Count the number of symbols on each line. Each group consists of 8 bits—a byte—which is the fundamental unit for character storage in digital computers.

### Hint 3
Each 8-bit binary string corresponds to an ASCII character. Calculate the numerical value of each 8-bit group (powers of 2 from $2^7$ down to $2^0$) or use the reference lookup table below:

#### Binary to ASCII Conversion Reference Table
| Binary (8-bit) | Hex | Decimal | ASCII Character |
|:---:|:---:|:---:|:---:|
| `00110000` | 0x30 | 48 | `0` |
| `00110001` | 0x31 | 49 | `1` |
| `00111001` | 0x39 | 57 | `9` |
| `01011111` | 0x5F | 95 | `_` (underscore) |
| `01100001` | 0x61 | 97 | `a` |
| `01100011` | 0x63 | 99 | `c` |
| `01100100` | 0x64 | 100 | `d` |
| `01100101` | 0x65 | 101 | `e` |
| `01100111` | 0x67 | 103 | `g` |
| `01101001` | 0x69 | 105 | `i` |
| `01101100` | 0x6C | 108 | `l` |
| `01101110` | 0x6E | 110 | `n` |
| `01110000` | 0x70 | 112 | `p` |
| `01110010` | 0x72 | 114 | `r` |
| `01110011` | 0x73 | 115 | `s` |
| `01110100` | 0x74 | 116 | `t` |
| `01110101` | 0x75 | 117 | `u` |
