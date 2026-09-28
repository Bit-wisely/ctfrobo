Solution: B04 - THE FILE THAT ISN'T THERE

Concept  
Linux filesystem hidden directories and recursive file discovery.

Walkthrough  
1. Navigate into `challenge/evidence/`.
2. Search through the evidence directory trees or list directory contents including hidden files and directories:
   ```bash
   ls -la logs/
   ```
3. Notice the hidden `.cache` directory inside `logs/`.
4. Inspect the contents of `logs/.cache/`:
   ```bash
   ls -la logs/.cache/
   ```
5. View the fragment file:
   ```bash
   cat logs/.cache/fragment
   ```
6. Extract the flag from the fragment content: `follow the evidence`.

Flag  
`follow the evidence`
