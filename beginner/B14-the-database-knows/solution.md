# Solution: B14 - THE DATABASE KNOWS

## Concept
Relational database queries correlate multiple tables through primary and foreign keys using `JOIN` operations. In SQL, filtering across multiple joined tables allows targeted record retrieval without manual table-by-table cross-referencing.

## Walkthrough
1. Inspect the schema of `challenge/company_vault.db`:
   ```bash
   sqlite3 challenge/company_vault.db ".schema"
   ```
2. Note the tables and relationships:
   - `departments (dept_id, dept_name, ...)`
   - `employees (emp_id, name, dept_id, role, clearance_level)`
   - `access_logs (log_id, emp_id, terminal_ip, access_time, action, status)`
   - `classified_vault (vault_id, log_id, secret_token)`
3. Execute the SQL join query with the incident parameters:
   ```bash
   sqlite3 challenge/company_vault.db "
   SELECT v.secret_token
   FROM classified_vault v
   JOIN access_logs a ON v.log_id = a.log_id
   JOIN employees e ON a.emp_id = e.emp_id
   JOIN departments d ON e.dept_id = d.dept_id
   WHERE d.dept_name = 'Cyber Defense'
     AND e.clearance_level = 'Level-5'
     AND a.action = 'OVERRIDE_AUTH';
   "
   ```
4. Or perform the query using Python:
   ```python
   import sqlite3
   conn = sqlite3.connect("challenge/company_vault.db")
   cur = conn.cursor()
   cur.execute("""
       SELECT v.secret_token
       FROM classified_vault v
       JOIN access_logs a ON v.log_id = a.log_id
       JOIN employees e ON a.emp_id = e.emp_id
       JOIN departments d ON e.dept_id = d.dept_id
       WHERE d.dept_name = 'Cyber Defense'
         AND e.clearance_level = 'Level-5'
         AND a.action = 'OVERRIDE_AUTH';
   """)
   print(cur.fetchone()[0])
   ```
5. Result retrieved:
   ```
   vault_record_extracted_90
   ```

## Flag
`vault_record_extracted_90`
