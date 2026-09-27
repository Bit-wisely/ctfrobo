#include <stdio.h>

int main() {
    printf("--- LOCKER EVENT LOG ---\n");
    printf("PUSH 80\n"); // 'P' (stack: [P])
    printf("PUSH 65\n"); // 'A' (stack: [P, A])
    printf("PUSH 71\n"); // 'G' (stack: [P, A, G])
    printf("PUSH 69\n"); // 'E' (stack: [P, A, G, E])
    printf("POP\n");     // pops 'E' -> 69
    printf("POP\n");     // pops 'G' -> 71
    printf("POP\n");     // pops 'A' -> 65
    printf("POP\n");     // pops 'P' -> 80
    printf("--- END OF LOG ---\n");
    printf("Hint: If read in reverse of pop (the original push order), what keyword points to a local file?\n");
    return 0;
}
