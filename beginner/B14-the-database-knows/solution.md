# Solution: B14 - THE DATABASE KNOWS

## Concept
Relational database querying connects tables across foreign keys. In SQL, joining `users` and `classified_vault` on `users.id = classified_vault.user_id` allows extracting attributes associated with specific user roles.

## Walkthrough
1. Inspect the SQL table schema and records in `challenge/database.sql`:
   - Account `charlie` has `id = 3` and `role = 'administrator'`.
2. Locate the matching record in `classified_vault`:
   ```sql
   INSERT INTO classified_vault (id, user_id, secret_note) VALUES
   (3, 3, 'vault_record_extracted_90');
   ```
3. Alternatively, execute `python3 challenge/query_db.py` to run the query in an in-memory SQLite instance:
   ```
   User: charlie | Note: vault_record_extracted_90
   ```
4. Recover the flag:
   ```
   vault_record_extracted_90
   ```

## Flag
`vault_record_extracted_90`
