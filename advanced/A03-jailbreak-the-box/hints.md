Hints: A03 - JAILBREAK THE BOX

1. The sandbox strictly filters command prefixes but passes arguments to `handle_echo`.
2. Inspect `challenge/jail.c` to see how arguments are compared.
3. Pass `echo $FLAG` or `echo --flag` to trigger the secret expansion.
