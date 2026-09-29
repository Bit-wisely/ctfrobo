# Hints: B03 - THE MACHINE SPEAKS

### Hint 1
Look at the raw program output. The data is serialized into lines containing only `0` and `1` characters.

### Hint 2
Count the number of symbols on each line. Each group consists of 8 bits—a byte—which is the fundamental unit for character storage in digital computers.

### Hint 3
Each 8-bit binary string corresponds to an ASCII character. You can convert the binary to hexadecimal or decimal, then use the reference table below:

#### Binary to ASCII Conversion Sample Reference
| Binary | Hex | ASCII | Binary | Hex | ASCII |
|:---:|:---:|:---:|:---:|:---:|:---:|
| 01100001 | 0x61 | a | 01110000 | 0x70 | p |
| 01100010 | 0x62 | b | 01110001 | 0x71 | q |
| 01100011 | 0x63 | c | 01110010 | 0x72 | r |
| 01100100 | 0x64 | d | 01110011 | 0x73 | s |
| 01100101 | 0x65 | e | 01110100 | 0x74 | t |
| 01100110 | 0x66 | f | 01110101 | 0x75 | u |
| 01100111 | 0x67 | g | 01110110 | 0x76 | v |
| 01101000 | 0x68 | h | 01110111 | 0x77 | w |
| 01101001 | 0x69 | i | 01111000 | 0x78 | x |
| 01101010 | 0x6a | j | 01111001 | 0x79 | y |
| 01101011 | 0x6b | k | 01111010 | 0x7a | z |
| 01101100 | 0x6c | l | 01011111 | 0x5f | _ |
| 01101101 | 0x6d | m | 00110000 | 0x30 | 0 |
| 01101110 | 0x6e | n | 00110001 | 0x31 | 1 |
| 01101111 | 0x6f | o | 00111001 | 0x39 | 9 |
