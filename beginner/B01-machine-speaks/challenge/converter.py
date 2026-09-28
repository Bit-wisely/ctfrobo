#!/usr/bin/env python3

def binary_to_ascii(binary_str):
    clean_bin = binary_str.strip().replace(" ", "")
    if len(clean_bin) % 8 != 0:
        print(f"[!] Warning: Input length ({len(clean_bin)}) is not a multiple of 8.")
    
    chars = []
    for i in range(0, len(clean_bin), 8):
        byte = clean_bin[i:i+8]
        if len(byte) == 8:
            chars.append(chr(int(byte, 2)))
    return "".join(chars)

def ascii_to_binary(text):
    return " ".join(format(ord(c), "08b") for c in text)

def main():
    print("=== Binary <-> ASCII Interactive Converter ===")
    print("1. Convert Binary to ASCII Text")
    print("2. Convert ASCII Text to Binary")
    print("3. Exit")
    
    while True:
        choice = input("\nSelect an option (1-3): ").strip()
        if choice == "1":
            raw = input("Enter binary string (e.g. 01100110 01101100...): ")
            try:
                result = binary_to_ascii(raw)
                print(f"[+] Converted ASCII: {result}")
            except Exception as e:
                print(f"[-] Error: {e}")
        elif choice == "2":
            text = input("Enter ASCII text: ")
            print(f"[+] Converted Binary: {ascii_to_binary(text)}")
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("[-] Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
