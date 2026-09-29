# B11 - THE WRONG FILE

| Attribute | Details |
| :--- | :--- |
| **Points** | 5 |
| **Category** | Beginner / Forensics |
| **Difficulty** | Intermediate Beginner |

---

## Scenario
An investigator recovered a file named `photo.jpg` from an unauthorized transfer directory. When desktop image previewers attempt to render the image, they crash or fail with corrupt stream errors. Forensic analysts suspect the sender deliberately renamed the file to masquerade as an image while concealing internal documents.

## Objective
Determine the true file format of `challenge/photo.jpg`, unpack or extract its embedded payload, and uncover the flag.

## Challenge Files
- `challenge/photo.jpg` — The masqueraded evidence file

## Execution Reference
```bash
# Inspect file format:
file challenge/photo.jpg
```

## Submission Format
Submit the recovered plaintext string directly (e.g. `secret_text_here`).
