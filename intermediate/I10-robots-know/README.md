I10 - ROBOTS KNOW

Points: 10
Category: Intermediate / Web Reconnaissance  

Challenge Overview  
The Robots Exclusion Standard utilizes a file named `robots.txt` placed in the web root directory to inform automated search engine crawlers which sections of a website should not be indexed. However, because `robots.txt` is publicly accessible to any web client, listing confidential or unlinked paths in `Disallow:` directives inadvertently discloses secret locations to attackers.

Participant Question  
The site has rules for search engines. Maybe those rules reveal something humans weren't supposed to find.

Clue  
Inspect `robots.txt` for disallowed directories and navigate to the hidden directory path.

Challenge Files  
- `challenge/website/index.html`
- `challenge/website/robots.txt`
- `challenge/website/hidden_admin_vault_9921/flag.html`

Flag Format  
`flag{...}`
