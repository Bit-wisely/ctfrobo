Solution: B11 - THE DATABASE KNOWS

Concept  
Relational database queries and SQL inspection.

Walkthrough  
1. Inspect `challenge/database.sql`.
2. Locate the insert statements for `classified_vault`:
   ```sql
   INSERT INTO classified_vault (id, user_id, secret_note) VALUES
   (3, 3, 'sqlite vault revealed');
   ```
3. Or inspect the query results to view the retrieved note: `sqlite vault revealed`.

Flag  
`sqlite vault revealed`
