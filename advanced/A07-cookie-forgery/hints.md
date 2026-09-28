Hints: A07 - COOKIE FORGERY

1. Inspect the browser cookies or HTTP request headers to examine how session state is stored.
2. Analyze the cookie structure to see if it is serialized or encoded without cryptographic signing or tamper protection.
3. Modify the decoded session claims to elevate privileges, re-encode the modified structure, and submit the forged cookie.
