**Hints: I14 - SQL QUESTION**

1. The tables are linked by `departments.dept_id = employees.dept_id` and `employees.emp_id = secure_vault.emp_id`.
2. Use `INNER JOIN` syntax to bridge all three tables in a single query.
3. Add `WHERE departments.name = 'Cyber Security' AND employees.role = 'Department Head'`.
