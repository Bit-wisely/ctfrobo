# Hints: B01 - BASE64 ISN'T ENCRYPTION

### Hint 1
Look closely at the characters in the message string. Notice the mix of uppercase, lowercase, numbers, and the distinctive trailing `=` characters.

### Hint 2
This string is not scrambled with an encryption key—it represents raw data mapped to a 64-character alphabet designed for safe transit over text-only protocols.

### Hint 3
When Base64 is decoded into bytes, each byte corresponds to an ASCII character. For reference, standard character-to-byte mappings follow the standard table below:

#### Character Reference Table
| Character | Decimal | Hexadecimal | Character | Decimal | Hexadecimal |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `a` - `z` | 97 - 122 | 0x61 - 0x7A | `0` - `9` | 48 - 57 | 0x30 - 0x39 |
| `A` - `Z` | 65 - 90  | 0x41 - 0x5A | `_` (underscore) | 95 | 0x5F |
| Space | 32 | 0x20 | `-` (dash) | 45 | 0x2D |
