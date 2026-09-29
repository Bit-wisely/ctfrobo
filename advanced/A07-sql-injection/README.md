# A07 - SQL INJECTION

Points: 20
Category: Advanced / SQL Injection

## Scenario
A portal login endpoint concatenates user-supplied credentials directly into dynamic database queries without sanitization. This enables visitors to reshape the SQL query structure.

## Objective
Craft a SQL injection payload that bypasses authentication and retrieves the administrator flag from the database.

Execution Reference
To run Python files: python filename.py
To compile and run C files: gcc filename.c -o output && ./output
