B14 - THE MISSING CHARACTER

Points: 5  
Category: Beginner / ASCII Encoding  

Challenge Overview  
Digital transmission channels occasionally suffer from single-byte data corruption or dropped packets. In this challenge, an ASCII byte array has been recovered with one missing value. Using contextual clues and character offsets, you must determine the dropped character and restore the message.

Participant Question  
A message was almost recovered. Every character is represented by a number. One character is missing. Find it and complete the message.

Clue  
The missing value equals `ord('a') + 10 = 107` (character 'k'). Insert 107 in place of `[MISSING]` to complete the array.

Challenge Files  
- `challenge/message.txt`

Flag Format  
`flag{...}`
