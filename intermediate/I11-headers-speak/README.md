I11 - HEADERS SPEAK

Points: 10
Category: Intermediate / HTTP Protocol  

Challenge Overview  
HTTP communication is divided into response headers and the response body. Web servers transmit important metadata inside headers, such as caching rules, content types, server software, and custom debugging flags. Checking both the body and the HTTP headers is critical in web assessments.

Participant Question  
You found the page. But the server sent more than the page. Listen to everything it says.

Clue  
Inspect the HTTP response headers using `curl -I` or by viewing `response.txt`. Look for custom headers starting with `X-`.

Challenge Files  
- `challenge/server/app.py`
- `challenge/server/response.txt`

Flag Format  
`flag{...}`
