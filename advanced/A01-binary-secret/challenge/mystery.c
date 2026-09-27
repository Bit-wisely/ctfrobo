#include <stdio.h>
#include <string.h>

// Decoy strings
const char *decoy1 = "flag{fake_flag_do_not_submit}";
const char *decoy2 = "admin:password123";

// Expected XOR-transformed byte constants
const unsigned char expected[] = {
    0x51, 0x5b, 0x56, 0x50, 0x4c,
    0x4d, 0x52, 0x56, 0x53, 0x68,
    0x4b, 0x5f, 0x52, 0x68, 0x55,
    0x5e, 0x59, 0x56, 0x4d, 0x46,
    0x4a
};

int check_passcode(const char *input) {
    int len = strlen(input);
    if (len != sizeof(expected)) {
        return 0;
    }
    for (int i = 0; i < len; i++) {
        if ((unsigned char)(input[i] ^ 0x37) != expected[i]) {
            return 0;
        }
    }
    return 1;
}

int main() {
    char buffer[128];
    printf("Enter authorization passcode: ");
    if (fgets(buffer, sizeof(buffer), stdin)) {
        buffer[strcspn(buffer, "\r\n")] = 0;
        if (check_passcode(buffer)) {
            printf("[+] ACCESS GRANTED! You cracked the binary logic.\n");
        } else {
            printf("[-] ACCESS DENIED! Invalid key.\n");
        }
    }
    return 0;
}
