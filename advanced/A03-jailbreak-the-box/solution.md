# Solution: A03 - JAILBREAK THE BOX

## Concept
Parser logic weaknesses and variable expansion in restricted execution environments.

## Walkthrough
1. Inspect `challenge/jail.c`.
2. Notice the argument check inside `handle_echo`:
   ```c
   if (strcmp(arg, "$FLAG") == 0 || strcmp(arg, "--flag") == 0) {
       printf("Secret Variable Expanded: %s\n", FLAG);
   }
   ```
3. Enter `echo $FLAG` into the shell.
4. Output: `escaped the box`.

## Flag
`escaped the box`
