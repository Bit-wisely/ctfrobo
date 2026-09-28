Hints: A09 - BLIND SQL

1. Blind SQL injection relies on boolean responses or status differences to infer database contents character by character.
2. Construct conditional SQL expressions that test individual character positions of the target table data.
3. Write an automation script that iterates over character positions and candidate characters to reconstruct the full secret.
