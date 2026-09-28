expected = [
    0x51, 0x5b, 0x56, 0x50, 0x4c,
    0x4d, 0x52, 0x56, 0x53, 0x17,
    0x4b, 0x5f, 0x52, 0x17, 0x55,
    0x5e, 0x59, 0x56, 0x4d, 0x46,
    0x4a
]

def check(user_input):
    if len(user_input) != len(expected):
        return False
    for i, char in enumerate(user_input):
        if (ord(char) ^ 0x37) != expected[i]:
            return False
    return True

if __name__ == '__main__':
    val = input("Enter authorization passcode: ")
    if check(val):
        print("[+] ACCESS GRANTED!")
    else:
        print("[-] ACCESS DENIED!")
