# Solution: B10 - THE SOURCE KNOWS

## Concept
Client-side web documents (HTML) can be inspected in their raw form. Developers often leave comments containing debug strings, internal endpoints, or credentials that are transmitted to every client but not rendered by the browser engine.

## Walkthrough
1. Inspect the source of `challenge/website/index.html`:
   ```bash
   cat challenge/website/index.html
   ```
2. Locate the HTML comment towards the bottom of the body tag:
   ```html
   <!-- SECRET_FLAG: source_whisper_found_83 -->
   ```
3. Extract the flag string:
   ```
   source_whisper_found_83
   ```

## Flag
`source_whisper_found_83`
