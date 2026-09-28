#include <stdio.h>
#include <string.h>

int main(void) {
    char input[32];
    const char *number = "54321";
    int expected = strlen(number);

    printf("================================\n");
    printf("        THE LOCKED DOOR\n");
    printf("================================\n\n");

    printf("The door is locked.\n\n");

    printf("The previous owner left some clues:\n\n");
    printf("12       -> 2\n");
    printf("1234     -> 4\n");
    printf("987      -> 3\n");
    printf("111111   -> 6\n\n");

    printf("What should this be?\n\n");
    printf("%s -> ?\n\n", number);

    printf("Enter the password: ");
    scanf("%31s", input);

    int answer = 0;

    for (int i = 0; input[i] != '\0'; i++) {
        if (input[i] < '0' || input[i] > '9') {
            printf("\nACCESS DENIED.\n");
            return 0;
        }

        answer = answer * 10 + (input[i] - '0');
    }

    if (answer == expected) {
        unsigned char message[] = {
            0x77, 0x65, 0x6c, 0x63, 0x6f,
            0x6d, 0x65, 0x20, 0x74, 0x6f,
            0x20, 0x43, 0x54, 0x46
        };

        printf("\nACCESS GRANTED!\n\n");
        printf("The door opens.\n\n");
        printf("Something was left behind:\n\n");

        for (size_t i = 0; i < sizeof(message); i++) {
            printf("%02x", message[i]);
        }

        printf("\n");
    } else {
        printf("\nACCESS DENIED.\n");
        printf("That's not the password.\n");
    }

    return 0;
}
