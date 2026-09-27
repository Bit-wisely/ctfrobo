**Hints: A08 - SQL INJECTION**

1. The SQL query formats the string using `f"SELECT ... WHERE username = '{username}' AND password = '{password}'"`.
2. Supplying a single quote terminates the string literal.
3. Pass `admin' --` into the username field to authenticate as the administrator without a password.
