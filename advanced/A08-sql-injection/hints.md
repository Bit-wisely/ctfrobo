Hints: A08 - SQL INJECTION

1. Authentication forms that dynamically concatenate user input into database queries are vulnerable to SQL injection.
2. Use special SQL characters such as single quotes to break out of the string literal in the query syntax.
3. Craft an input that comments out the remainder of the query condition so authentication succeeds without validating the password.
