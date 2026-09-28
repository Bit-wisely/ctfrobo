Solution: B06 - THE POINTER'S SECRET

Concept  
C memory addresses, referencing, and double pointer dereferencing.

Walkthrough  
1. Inspect `challenge/pointer.c`.
2. Trace the pointer variables:
   - `p1` points to `"try again friend"`
   - `p2` points to `"pointer indirection found"`
   - `ptr` is reassigned: `ptr = &p2`
3. Dereferencing `ptr` resolves to `p2`, which holds `"pointer indirection found"`.

Flag  
`flag{pointer indirection found}`
