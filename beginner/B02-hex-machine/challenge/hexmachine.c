#include <stdio.h>

int main() {
    unsigned char bytes[] = {
        0x66, 0x6c, 0x61, 0x67, 0x7b,
        0x68, 0x65, 0x78, 0x20,
        0x6d, 0x61, 0x63, 0x68, 0x69, 0x6e, 0x65,
        0x7d
    };
    int count = sizeof(bytes) / sizeof(bytes[0]);
    for (int i = 0; i < count; i++) {
        printf("%02x ", bytes[i]);
    }
    printf("\n");
    return 0;
}
