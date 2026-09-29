I01 - THE FILE THAT PRETENDS

Points: 10
Category: Intermediate / File Signatures & Magic Bytes

Scenario
A suspicious file named notes.txt was recovered from an exfiltration directory. Although the operating system treats it as plain text based on its extension, applications fail to parse it properly.

Objective
Analyze the raw header bytes, restore the authentic file signature, and identify the embedded flag.

Execution Reference
To run Python files: python filename.py
To compile and run C files: gcc filename.c -o output && ./output
