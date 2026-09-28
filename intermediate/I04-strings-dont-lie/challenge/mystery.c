#include <stdio.h>
#include <string.h>

const char *banner = "--- Welcome to the System Security Checker v1.0 ---";
const char *author = "DevOps Security Team";
const char *secret_key = "strings revealed";
const char *decoy_data = "DEBUG_MODE_DISABLED_IN_PROD";

int main() {
    printf("%s\n", banner);
    printf("Access Denied: Authentication module inactive.\n");
    return 0;
}
