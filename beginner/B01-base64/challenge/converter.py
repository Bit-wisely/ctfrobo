#!/usr/bin/env python3
import base64

def main():
    print("=== Base64 Interactive Tool ===")
    print("1. Decode Base64 string to Text")
    print("2. Encode Text to Base64")
    print("3. Exit")
    
    while True:
        choice = input("\nSelect an option (1-3): ").strip()
        if choice == "1":
            b64_str = input("Enter Base64 string: ").strip()
            try:
                decoded = base64.b64decode(b64_str).decode("utf-8", errors="replace")
                print(f"[+] Decoded text: {decoded}")
            except Exception as e:
                print(f"[-] Decode error: {e}")
        elif choice == "2":
            text = input("Enter plain text: ")
            encoded = base64.b64encode(text.encode()).decode()
            print(f"[+] Encoded Base64: {encoded}")
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("[-] Invalid option.")

if __name__ == "__main__":
    main()
