A14 - WEB CHAIN

Points: 20
Category: Advanced / Web Exploitation Chain  

Challenge Overview  
Real-world application security breaches rarely rely on a single critical bug; instead, attackers frequently combine a chain of low-to-medium severity oversights. In this challenge, an attacker must inspect client-facing HTML assets to discover unlinked backend paths, probe hidden endpoints to extract leaked developer debug headers, and finally supply those internal credentials to invoke administrative API routines.

Participant Question  
The first door isn't the last. Every discovery gives you another place to look. Keep following the trail.

Clue  
Inspect the HTML source code on the homepage for an internal developer comment disclosing `/secret_api_gateway_v1/`. Query that path to find the `X-Debug-Key` header, then submit a POST request to `/api/execute` containing that header key.

Challenge Files  
- `challenge/app/app.py`
- `challenge/app/templates/index.html`

Flag Format  
`flag{...}`

