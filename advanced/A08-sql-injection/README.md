A08 - SQL INJECTION

Points: 20
Category: Advanced / SQL Injection  

Challenge Overview  
SQL Injection (SQLi) occurs when untrusted user input is directly concatenated into a dynamic SQL query without parameterization or escaping. This flaw enables attackers to manipulate query syntax, bypass authentication checks, read unauthorized records, or execute administrative commands.

Participant Question  
The login form asks a question. The database answers it. What happens when you change the question?

Clue  
Break out of the username string using a single quote (`'`), followed by SQL comment symbols (`--`) to neutralize the password check.

Challenge Files  
- `challenge/app/app.py`
- `challenge/app/database.sql`
- `challenge/app/templates/login.html`

Flag Format  
`flag{...}`
