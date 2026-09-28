def main():
    print("=== Secure Firmware Terminal ===")
    print("Type 'help' for commands.")
    while True:
        try:
            cmd = input("sec-cli> ").strip()
        except EOFError:
            break

        if cmd == "help":
            print("Available Commands:\n  help\n  status\n  version\n  exit")
        elif cmd == "status":
            print("[*] System operational.")
        elif cmd == "version":
            print("Firmware Monitor v3.8.1")
        elif cmd == "exit":
            break
        elif cmd in ["backdoor", "__backdoor_access_99__"]:
            print("[!] BACKDOOR ACTIVATED.")
            print("FLAG: backdoor found")
        else:
            print(f"Unknown command: {cmd}")

if __name__ == "__main__":
    main()
