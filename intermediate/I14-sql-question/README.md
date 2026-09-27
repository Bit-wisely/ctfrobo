**I14 - SQL QUESTION**

**Points**: 350  
**Category**: Intermediate / Relational SQL  

**Challenge Overview**  
In normalized database schemas, related business information is distributed across multiple distinct tables connected through primary and foreign keys. Answering complex security and operational questions requires joining multiple tables to synthesize the complete record.

**Participant Question**  
One table has names. Another has departments. Another has records. The information you need isn't in one place.

**Clue**  
Write a multi-table SQL `INNER JOIN` query connecting `departments`, `employees`, and `secure_vault`. Filter for the `Department Head` of the `Cyber Security` department.

**Challenge Files**  
- `challenge/database.sql`
- `challenge/query.py`

**Flag Format**  
`flag{...}`
