#!/usr/bin/env python3

def xor_bytes(data, key):
    return bytes([b ^ key for b in data])

def main():
    print("=== Bitwise XOR Interactive Helper ===")
    print("1. XOR String with Key (Integer or Hex)")
    print("2. XOR Hex Array with Key")
    print("3. Exit")
    
    while True:
        choice = input("\nSelect an option (1-3): ").strip()
        if choice == "1":
            text = input("Enter text to XOR: ")
            key_str = input("Enter key (e.g. 0x5A or 90): ").strip()
            key = int(key_str, 16) if key_str.startswith("0x") else int(key_str)
            res = xor_bytes(text.encode(), key)
            print(f"[+] Result (Hex): {res.hex()}")
            print(f"[+] Result (ASCII/Repr): {res}")
        elif choice == "2":
            hex_data = input("Enter hex string (e.g. 3c363b3d...): ").strip()
            key_str = input("Enter key (e.g. 0x5A or 90): ").strip()
            key = int(key_str, 16) if key_str.startswith("0x") else int(key_str)
            res = xor_bytes(bytes.fromhex(hex_data), key)
            print(f"[+] Result (Text): {res.decode('utf-8', errors='replace')}")
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("[-] Invalid choice.")

if __name__ == "__main__":
    main()
