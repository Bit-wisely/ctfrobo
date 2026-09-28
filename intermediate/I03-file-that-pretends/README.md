I03 - THE FILE THAT PRETENDS

Points: 10
Category: Intermediate / File Signatures

Scenario
An investigator found a suspicious file labeled as plain text notes, but standard text editors fail to render its contents properly. Operating systems and analysis tools often rely on true file headers rather than surface extensions.

Objective
Inspect the file's underlying magic bytes and header structure to identify its true file format and extract the flag.

Execution Reference
To run Python files: python filename.py
To compile and run C files: gcc filename.c -o output && ./output
