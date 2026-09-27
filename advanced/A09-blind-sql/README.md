A09 - BLIND SQL

Points: 20
Category: Advanced / Blind SQL Injection  

Challenge Overview  
Blind SQL Injection occurs when an application is vulnerable to SQL injection but does not return data rows or SQL errors directly in the HTTP response. Instead, the application only responds with a generic Boolean indicator (such as `{"exists": true}` vs `{"exists": false}`). Attackers infer the secret character-by-character by asking conditional true/false questions.

Participant Question  
The database doesn't show you the answer. It only tells you whether your question was right or wrong. Ask better questions.

Clue  
Use Boolean conditions with SQLite's `SUBSTR()` function (e.g. `admin' AND SUBSTR((SELECT secret_val FROM secrets), 1, 1) = 'a' --`) to extract each character based on true/false responses.

Challenge Files  
- `challenge/app/app.py`
- `challenge/app/database.sql`
- `challenge/app/exploit_demo.py`

Flag Format  
`flag{...}`
