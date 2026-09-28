#!/usr/bin/env python3

def main():
    number = "54321"
    expected = len(number)

    print("================================")
    print("        THE LOCKED DOOR")
    print("================================\n")
    print("The door is locked.\n")
    print("The previous owner left some clues:\n")
    print("12       -> 2")
    print("1234     -> 4")
    print("987      -> 3")
    print("111111   -> 6\n")
    print("What should this be?\n")
    print(f"{number} -> ?\n")

    user_input = input("Enter the password: ").strip()

    if not user_input.isdigit():
        print("\nACCESS DENIED.")
        return

    answer = int(user_input)

    if answer == expected:
        message = bytes([
            0x77, 0x65, 0x6c, 0x63, 0x6f,
            0x6d, 0x65, 0x20, 0x74, 0x6f,
            0x20, 0x43, 0x54, 0x46
        ])
        print("\nACCESS GRANTED!\n")
        print("The door opens.\n")
        print("Something was left behind:\n")
        print(message.hex())
    else:
        print("\nACCESS DENIED.")
        print("That's not the password.")

if __name__ == "__main__":
    main()
