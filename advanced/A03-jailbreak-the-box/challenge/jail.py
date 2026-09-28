FLAG = "escaped the box"

def main():
    print("=== RESTRICTED SHELL JAIL ===")
    print("Allowed commands: echo <text>, time, help, exit")
    while True:
        try:
            line = input("jail$ ").strip()
        except EOFError:
            break

        if line.startswith("echo "):
            arg = line[5:]
            if arg in ["$FLAG", "--flag"]:
                print(f"Secret Variable Expanded: {FLAG}")
            else:
                print(arg)
        elif line == "help":
            print("Commands: echo <text>, time, help, exit")
        elif line == "time":
            print("Current system tick: 1700000000")
        elif line == "exit":
            break
        else:
            print(f"Error: Command '{line}' is prohibited in this sandbox.")

if __name__ == "__main__":
    main()
