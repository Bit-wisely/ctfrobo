Solution: B15 - THE CHAIN

Concept  
Sequential puzzle solving and file linking.

Walkthrough  
1. Decode `challenge/start.bin` from binary to ASCII:
   `01100011 01101100 01110101 01100101 00101110 01110100 01111000 01110100` -> `clue.txt`
2. Open `challenge/clue.txt` which points to `final_flag.txt`.
3. Open `challenge/final_flag.txt` to read the flag.

Flag  
`flag{chain reaction beginner}`
