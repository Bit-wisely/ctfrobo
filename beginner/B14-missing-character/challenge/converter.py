#!/usr/bin/env python3

def main():
    print("=== ASCII Code & Character Converter ===")
    print("1. Convert Characters to ASCII Decimal & Hex")
    print("2. Convert ASCII Numbers (Decimal/Hex) to Characters")
    print("3. Shift / Offset ASCII Characters")
    print("4. Exit")
    
    while True:
        choice = input("\nSelect an option (1-4): ").strip()
        if choice == "1":
            s = input("Enter text: ")
            print("Char -> Decimal (Hex):")
            for c in s:
                print(f"  '{c}' -> {ord(c)} (0x{ord(c):02x})")
        elif choice == "2":
            nums = input("Enter space-separated ASCII numbers: ").strip().split()
            chars = []
            for n in nums:
                val = int(n, 16) if n.startswith("0x") else int(n)
                chars.append(chr(val))
            print(f"[+] Output string: {''.join(chars)}")
        elif choice == "3":
            s = input("Enter text: ")
            offset = int(input("Enter integer offset to add/subtract: "))
            res = "".join(chr(ord(c) + offset) for c in s)
            print(f"[+] Shifted text: {res}")
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("[-] Invalid choice.")

if __name__ == "__main__":
    main()
