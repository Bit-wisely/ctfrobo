#!/usr/bin/env python3

def main():
    print("=== Bitwise XOR Tool (ASCII & Decimal) ===")
    print("1. Decode Decimal Numbers to ASCII Text (XOR with Key)")
    print("2. Encode ASCII Text to Decimal Numbers (XOR with Key)")
    print("3. Exit")
    
    while True:
        choice = input("\nSelect an option (1-3): ").strip()
        if choice == "1":
            raw_nums = input("Enter decimal numbers separated by spaces: ").strip()
            key_str = input("Enter key (integer): ").strip()
            try:
                nums = [int(x) for x in raw_nums.split()]
                key = int(key_str)
                decoded_chars = [chr(n ^ key) for n in nums]
                result_text = "".join(decoded_chars)
                print(f"[+] Decoded ASCII Text: {result_text}")
            except Exception as e:
                print(f"[-] Error: {e}")
        elif choice == "2":
            text = input("Enter plain ASCII text: ")
            key_str = input("Enter key (integer): ").strip()
            try:
                key = int(key_str)
                encoded_nums = [str(ord(c) ^ key) for c in text]
                print(f"[+] Encoded Decimal Numbers: {' '.join(encoded_nums)}")
            except Exception as e:
                print(f"[-] Error: {e}")
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("[-] Invalid choice.")

if __name__ == "__main__":
    main()
