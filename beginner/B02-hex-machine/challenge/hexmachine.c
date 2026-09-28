#include <stdio.h>

int main() {
    unsigned char bytes[] = {
        0x68, 0x65, 0x78, 0x20,
        0x6d, 0x61, 0x63, 0x68, 0x69, 0x6e, 0x65
    };
    int count = sizeof(bytes) / sizeof(bytes[0]);
    for (int i = 0; i < count; i++) {
        printf("%02x ", bytes[i]);
    }
    printf("\n");
    return 0;
}
