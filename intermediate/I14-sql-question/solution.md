**Solution: I14 - SQL QUESTION**

**Concept**  
Relational SQL JOIN operations across foreign keys.

**Walkthrough**  
1. Inspect `challenge/database.sql`.
2. Execute the relational join query:
   ```sql
   SELECT secure_vault.secret_value
   FROM departments
   JOIN employees ON departments.dept_id = employees.dept_id
   JOIN secure_vault ON employees.emp_id = secure_vault.emp_id
   WHERE departments.name = 'Cyber Security' AND employees.role = 'Department Head';
   ```
3. Retrieve the flag: `flag{relational_database_joined}`.

**Flag**  
`flag{relational_database_joined}`
