**Solution: B07 - THE SEARCHER**

**Concept**  
Binary search step execution and complexity.

**Walkthrough**  
1. Search array for target value `1131`:
   - Step 1: index 49 (val 645) -> search [50, 99]
   - Step 2: index 74 (val 1014) -> search [75, 99]
   - Step 3: index 87 (val 1205) -> search [75, 86]
   - Step 4: index 80 (val 1102) -> search [81, 86]
   - Step 5: index 83 (val 1146) -> search [81, 82]
   - Step 6: index 81 (val 1116) -> search [82, 82]
   - Step 7: index 82 (val 1131) -> Match found.
2. Total comparisons made: 7.

**Flag**  
`flag{binary_search_7_steps}`
