#include <stdio.h>

int main() {
    printf("--- LOCKER EVENT LOG ---\n");
    printf("PUSH 80\n");
    printf("PUSH 65\n");
    printf("PUSH 71\n");
    printf("PUSH 69\n");
    printf("POP\n");
    printf("POP\n");
    printf("POP\n");
    printf("POP\n");
    printf("--- END OF LOG ---\n");
    printf("Hint: If read in reverse of pop (the original push order), what keyword points to a local file?\n");
    return 0;
}
