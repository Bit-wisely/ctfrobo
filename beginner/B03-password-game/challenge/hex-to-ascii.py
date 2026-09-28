#!/usr/bin/env python3

hex_input = input("Enter hexadecimal: ").strip()

try:
    result = bytes.fromhex(hex_input).decode("ascii")
    print(result)
except ValueError:
    print("Invalid hexadecimal input.")
except UnicodeDecodeError:
    print("Input does not represent valid ASCII text.")
