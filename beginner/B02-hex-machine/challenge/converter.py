#!/usr/bin/env python3

def hex_to_ascii(hex_str):
    clean_hex = hex_str.strip().replace(" ", "").replace("0x", "")
    return bytes.fromhex(clean_hex).decode("utf-8", errors="replace")

def ascii_to_hex(text):
    return text.encode("utf-8").hex()

def main():
    print("=== Hexadecimal <-> ASCII Interactive Converter ===")
    print("1. Convert Hex to ASCII Text")
    print("2. Convert ASCII Text to Hex")
    print("3. Exit")
    
    while True:
        choice = input("\nSelect an option (1-3): ").strip()
        if choice == "1":
            raw = input("Enter hex string (e.g. 666c6167... or 66 6c 61 67...): ")
            try:
                result = hex_to_ascii(raw)
                print(f"[+] Converted ASCII: {result}")
            except Exception as e:
                print(f"[-] Error: {e}")
        elif choice == "2":
            text = input("Enter ASCII text: ")
            print(f"[+] Converted Hex: {ascii_to_hex(text)}")
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("[-] Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
