#!/usr/bin/env python3
def caesar_shift(text, shift):
    result = []
    for c in text:
        if 'a' <= c <= 'z':
            result.append(chr((ord(c) - ord('a') + shift) % 26 + ord('a')))
        elif 'A' <= c <= 'Z':
            result.append(chr((ord(c) - ord('A') + shift) % 26 + ord('A')))
        else:
            result.append(c)
    return "".join(result)

def main():
    print("=== Caesar Cipher Interactive Tool ===")
    print("1. Decrypt / Shift by specific offset")
    print("2. Brute-force all 26 possible shifts")
    print("3. Exit")
    
    while True:
        choice = input("\nSelect an option (1-3): ").strip()
        if choice == "1":
            text = input("Enter cipher text: ")
            shift = int(input("Enter shift offset (e.g. 13 or -13): "))
            print(f"[+] Result: {caesar_shift(text, shift)}")
        elif choice == "2":
            text = input("Enter cipher text: ")
            print("\nAll 26 shift rotations:")
            for s in range(1, 26):
                print(f"  Shift {s:02d}: {caesar_shift(text, s)}")
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("[-] Invalid option.")

if __name__ == "__main__":
    main()
