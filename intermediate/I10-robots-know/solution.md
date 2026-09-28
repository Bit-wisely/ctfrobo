Solution: I10 - ROBOTS KNOW

Concept  
Information disclosure and endpoint enumeration via `robots.txt`.

Walkthrough  
1. Inspect `challenge/website/robots.txt`:
   ```text
   Disallow: /hidden_admin_vault_9921/
   ```
2. Open `challenge/website/hidden_admin_vault_9921/flag.html`.
3. Retrieve the flag: `flag{robots keep no secrets}`.

Flag  
`flag{robots keep no secrets}`
