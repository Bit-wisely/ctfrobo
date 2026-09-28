# A10 - COMMAND INJECTION

Points: 20
Category: Advanced / Command Injection

## Scenario
A system diagnostic utility accepts user input and incorporates it directly into a host shell command execution. The application fails to sanitize shell metacharacters before execution.

## Objective
Inject arbitrary operating system commands through the input parameter to read the protected flag file.

Execution Reference
To run Python files: python filename.py
To compile and run C files: gcc filename.c -o output && ./output
