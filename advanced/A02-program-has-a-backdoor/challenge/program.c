#include <stdio.h>
#include <string.h>

void print_help() {
    printf("Available Commands:\n");
    printf("  help    - Show this help menu\n");
    printf("  status  - Check operational status\n");
    printf("  version - Print software release\n");
    printf("  exit    - Terminate terminal session\n");
}

void print_status() {
    printf("[*] System operational. All services running normally.\n");
}

void print_version() {
    printf("Firmware Monitor v3.8.1 (Enterprise Edition)\n");
}

void secret_backdoor() {
    printf("[!] BACKDOOR ACTIVATED. Administrative Override Triggered!\n");
    printf("FLAG: backdoor found\n");
}

int main() {
    char cmd[64];
    printf("=== Secure Firmware Terminal ===\nType 'help' for commands.\n");
    while (1) {
        printf("sec-cli> ");
        if (!fgets(cmd, sizeof(cmd), stdin)) break;
        cmd[strcspn(cmd, "\r\n")] = 0;

        if (strcmp(cmd, "help") == 0) {
            print_help();
        } else if (strcmp(cmd, "status") == 0) {
            print_status();
        } else if (strcmp(cmd, "version") == 0) {
            print_version();
        } else if (strcmp(cmd, "exit") == 0) {
            break;
        } else if (strcmp(cmd, "__backdoor_access_99__") == 0 || strcmp(cmd, "backdoor") == 0) {
            secret_backdoor();
        } else {
            printf("Unknown command: %s\n", cmd);
        }
    }
    return 0;
}
