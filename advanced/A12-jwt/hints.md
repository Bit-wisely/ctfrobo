**Hints: A12 - JWT**

1. A JWT is constructed in three parts separated by dots: `<header>.<payload>.<signature>`.
2. The verification logic in `app.py` accepts tokens where `header.alg` equals `"none"`.
3. Construct an unsigned token ending with a trailing dot: `eyJhbGciOiJub25lIiwidHlwIjoiSldUIn0.eyJ1c2VyIjoiYWRtaW4iLCJyb2xlIjoiYWRtaW4ifQ.`.
