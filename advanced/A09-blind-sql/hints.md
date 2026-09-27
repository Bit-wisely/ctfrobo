**Hints: A09 - BLIND SQL**

1. The API returns `{"exists": true}` when the SQL condition evaluates to True, and `{"exists": false}` otherwise.
2. Formulate subqueries using `SUBSTR((SELECT secret_val FROM secrets), pos, 1) = '<char>'`.
3. Automate the search loop across character sets `a-z_` using a Python script.
