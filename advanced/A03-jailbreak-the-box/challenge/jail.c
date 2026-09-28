#include <stdio.h>
#include <string.h>

const char *FLAG = "flag{escaped the box}";

void handle_echo(char *arg) {
    if (strcmp(arg, "$FLAG") == 0 || strcmp(arg, "--flag") == 0) {
        printf("Secret Variable Expanded: %s\n", FLAG);
    } else {
        printf("%s\n", arg);
    }
}

int main() {
    char line[128];
    printf("=== RESTRICTED SHELL JAIL ===\nAllowed commands: echo <text>, time, help, exit\n");
    while (1) {
        printf("jail$ ");
        if (!fgets(line, sizeof(line), stdin)) break;
        line[strcspn(line, "\r\n")] = 0;

        if (strncmp(line, "echo ", 5) == 0) {
            handle_echo(line + 5);
        } else if (strcmp(line, "help") == 0) {
            printf("Commands: echo <text>, time, help, exit\n");
        } else if (strcmp(line, "time") == 0) {
            printf("Current system tick: 1700000000\n");
        } else if (strcmp(line, "exit") == 0) {
            break;
        } else {
            printf("Error: Command '%s' is prohibited in this sandbox.\n", line);
        }
    }
    return 0;
}
