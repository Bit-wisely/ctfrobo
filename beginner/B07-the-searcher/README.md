B07 - THE SEARCHER

Points: 5  
Category: Beginner / Algorithms  

Challenge Overview  
Binary search is a logarithmic time algorithm that efficiently locates an element in a sorted list. By comparing the target value to the middle element, it eliminates half of the remaining elements at each step. In this challenge, your task is to trace a binary search for target value 1131 and count the total number of comparisons.

Participant Question  
The list is already sorted. The searcher doesn't check every item. It keeps cutting the search space in half. How many checks does it need to find the target?

Clue  
Use integer midpoint indexing: `mid = (low + high) // 2`. Count every time the algorithm checks `arr[mid]`.

Challenge Files  
- `challenge/numbers.txt`
- `challenge/instructions.txt`

Flag Format  
`flag{binary_search_<N>_steps}`
