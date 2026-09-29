# Hints: B03 - BASE64 ISN'T ENCRYPTION

### Hint 1
Look closely at the characters in the message string. Notice the mix of uppercase, lowercase, numbers, and the distinctive trailing `=` characters.

### Hint 2
This string is not scrambled with an encryption key—it represents raw data mapped to a 64-character alphabet designed for safe transit over text-only protocols.

### Hint 3
Base64 groups 6 bits per character according to the standard index mapping table below. In Linux, standard terminal utilities like `base64` or Python's `base64` library can invert this mapping:

#### Base64 Index Table Reference
| Index Range | Characters | Binary Representation |
|:---:|:---:|:---:|
| 0 – 25 | `A` – `Z` | `000000` – `011001` |
| 26 – 51 | `a` – `z` | `011010` – `110011` |
| 52 – 61 | `0` – `9` | `110100` – `111101` |
| 62 | `+` | `111110` |
| 63 | `/` | `111111` |
| Padding | `=` | Zero-bit alignment |
