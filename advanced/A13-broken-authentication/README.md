# A13 - BROKEN AUTHENTICATION

Points: 20
Category: Advanced / Authentication Flaws

## Scenario
An account recovery portal issues password reset tokens based on predictable, deterministic algorithms rather than cryptographically secure random values.

## Objective
Analyze the token generation logic, compute a valid recovery token for the administrator account, and capture the flag.

Execution Reference
To run Python files: python filename.py
To compile and run C files: gcc filename.c -o output && ./output
