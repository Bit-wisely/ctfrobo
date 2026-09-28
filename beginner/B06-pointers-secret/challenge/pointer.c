#include <stdio.h>

int main() {
    char fake_target[] = "try again friend";
    char real_target[] = "pointer indirection found";
    
    char *p1 = fake_target;
    char *p2 = real_target;
    char **ptr = &p1;

    ptr = &p2;

    printf("The secret pointer resolves to: %s\n", *ptr);
    printf("Flag: %s\n", *ptr);

    return 0;
}
