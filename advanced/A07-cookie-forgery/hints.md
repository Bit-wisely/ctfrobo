**Hints: A07 - COOKIE FORGERY**

1. Base64-decode the session cookie string to inspect the JSON dictionary.
2. Update the JSON payload: `{"user": "admin", "role": "admin"}`.
3. Encode the updated JSON string into Base64 (`eyJ1c2VyIjogImFkbWluIiwgInJvbGUiOiAiYWRtaW4ifQ==`) and supply it as the `session` cookie.
