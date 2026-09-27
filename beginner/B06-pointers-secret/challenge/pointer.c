#include <stdio.h>

int main() {
    char fake_target[] = "try_again_friend";
    char real_target[] = "pointer_indirection_found";
    
    char *p1 = fake_target;
    char *p2 = real_target;
    char **ptr = &p1;

    // Pointer redirection
    ptr = &p2;

    printf("The secret pointer resolves to: %s\n", *ptr);
    printf("Flag structure: flag{%s}\n", *ptr);

    return 0;
}
