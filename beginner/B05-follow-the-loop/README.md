**B05 - FOLLOW THE LOOP**

**Points**: 150  
**Category**: Beginner / Program Tracing  

**Challenge Overview**  
Static program analysis and dynamic code tracing are core reverse engineering skills. In this challenge, a state variable undergoes continuous transformations through arithmetic modulations, conditional branches, and bitwise logic across 24 iterations.

**Participant Question**  
This program keeps changing the same value. Don't just run it. Follow what it does. What value does it finally reach?

**Clue**  
Trace the conditional hierarchy carefully. Any iteration number divisible by 3 triggers the first branch, taking precedence over even numbers.

**Challenge Files**  
- `challenge/trace.py`

**Flag Format**  
`flag{loop_trace_<FINAL_VALUE>}`
