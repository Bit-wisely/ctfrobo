I08 - COOKIE TROUBLE

Points: 10
Category: Intermediate / Web Security  

Challenge Overview  
HTTP cookies allow web applications to maintain state across stateless HTTP requests. If a server relies on client-controlled cookies to make authorization decisions without server-side validation or cryptographic signing, users can tamper with their cookie values to impersonate other roles.

Participant Question  
The server thinks you are just a normal user. But it trusts something you carry. Find out what the server believes about you.

Clue  
Inspect the HTTP request cookies. Change `role=user` to `role=admin` to elevate permissions.

Challenge Files  
- `challenge/app/app.py`
- `challenge/app/templates/index.html`

Flag Format  
`flag{...}`
