Solution: B08 - READ BETWEEN THE LINES

Concept
Pattern matching and text filtering in large log files using command-line search tools.

Walkthrough
1. Inspect the log file size and structure:
   cat logs/system.log
2. Recognize that manual analysis across hundreds of lines is inefficient.
3. Use a search tool like grep to filter for challenge markers or suspicious tokens:
   grep "CTF" logs/system.log
4. The command isolates the matching line:
   2026-09-28 11:43:35 CTF-MESSAGE: The answer is silent_witness
5. Extract the final answer: silent_witness.

Flag
silent_witness
