**Solution: B06 - THE POINTER'S SECRET**

**Concept**  
C memory addresses, referencing, and double pointer dereferencing.

**Walkthrough**  
1. Inspect `challenge/pointer.c`.
2. Trace the pointer variables:
   - `p1` points to `"try_again_friend"`
   - `p2` points to `"pointer_indirection_found"`
   - `ptr` is reassigned: `ptr = &p2`
3. Dereferencing `*ptr` resolves to `p2`, which holds `"pointer_indirection_found"`.

**Flag**  
`flag{pointer_indirection_found}`
