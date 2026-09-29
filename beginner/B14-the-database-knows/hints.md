# Hints: B14 - THE DATABASE KNOWS

### Hint 1
Open the SQLite database file using `sqlite3 challenge/company_vault.db` (or Python's `sqlite3` library) and inspect the available tables and foreign keys using `.tables` and `.schema`.

### Hint 2
The database is relational: `departments` relates to `employees` through `dept_id`, `employees` relates to `access_logs` through `emp_id`, and `access_logs` relates to `classified_vault` through `log_id`.

### Hint 3
Write a SQL query using `JOIN` statements across these four tables, filtering on the department name (`Cyber Defense`), employee clearance (`Level-5`), and audit action (`OVERRIDE_AUTH`) to isolate the unique vault entry.
