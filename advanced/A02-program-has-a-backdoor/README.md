# A02 - THE PROGRAM HAS A BACKDOOR

Points: 20
Category: Advanced / Reverse Engineering

## Scenario
A proprietary administrative utility presents a standard command menu to ordinary users. Hidden deep inside its dispatch routines lies an undocumented diagnostic interface.

## Objective
Deconstruct the command parsing logic to discover the secret backdoor and trigger the flag routine.

Execution Reference
To run Python files: python filename.py
To compile and run C files: gcc filename.c -o output && ./output
