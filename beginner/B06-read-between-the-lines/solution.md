# Solution: B06 - READ BETWEEN THE LINES

## Concept
Linux text utilities like `grep` enable rapid searching through high-volume log streams for non-standard keywords, flags, or markers.

## Walkthrough
1. Examine `challenge/logs/system.log` using text filtering:
   ```bash
   grep "CTF-MESSAGE" challenge/logs/system.log
   # or search for "answer"
   grep -i "answer" challenge/logs/system.log
   ```
2. The matched line output is:
   ```
   2026-09-28 11:43:35 CTF-MESSAGE: The answer is trace_vector_active_91
   ```
3. The flag is:
   ```
   trace_vector_active_91
   ```

## Flag
`trace_vector_active_91`
