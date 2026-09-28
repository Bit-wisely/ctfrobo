A11 - PATH TRAVERSAL

Points: 20
Category: Advanced / Path Traversal

Scenario
A document downloading portal accepts file path parameters to serve public files. The application does not properly validate or constrain requests to the intended public directory.

Objective
Use path traversal techniques to navigate outside the allowed public folder and read the restricted flag file.

Challenge Files
- `challenge/app/app.py`
- `challenge/app/public/sample.txt`
- `challenge/app/secret/flag.txt`

Flag Format
`flag{...}`
