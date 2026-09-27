**Solution: I11 - HEADERS SPEAK**

**Concept**  
HTTP response header inspection and metadata disclosure.

**Walkthrough**  
1. Inspect the response headers in `challenge/server/response.txt`:
   ```http
   HTTP/1.1 200 OK
   X-CTF-Message: flag{headers_contain_secrets}
   Content-Type: text/plain
   ```
2. Extract the flag from the `X-CTF-Message` header value.

**Flag**  
`flag{headers_contain_secrets}`
