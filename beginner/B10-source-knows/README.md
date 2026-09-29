# B10 - THE SOURCE KNOWS

| Attribute | Details |
| :--- | :--- |
| **Points** | 5 |
| **Category** | Beginner / Web Reconnaissance |
| **Difficulty** | Introductory |

---

## Scenario
A software team put up a temporary splash page indicating system maintenance. While the visible frontend displays minimal text to regular users, client-side web technologies deliver entire markup files to the browser, potentially exposing comments or draft notes left by developers before publishing.

## Objective
Examine the website files in `challenge/website/`, inspect the underlying HTML source code, and recover the flag.

## Challenge Files
- `challenge/website/index.html` — Published maintenance landing page

## Execution Reference
```bash
# View source in terminal:
cat challenge/website/index.html
```

## Submission Format
Submit the recovered plaintext string directly (e.g. `secret_text_here`).
