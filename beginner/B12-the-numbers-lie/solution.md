Solution: B12 - THE NUMBERS LIE

Concept  
Integer division truncation vs floating point arithmetic.

Walkthrough  
1. Inspect `challenge/numbers.py`.
2. Notice how dividing two integers (`10 // 3`) drops the decimal portion, resulting in 3.
3. Multiplying back by 3 yields 9 instead of the original 10.
4. The key concept is `integer_division_precision`.

Flag  
`flag{integer_division_precision}`
