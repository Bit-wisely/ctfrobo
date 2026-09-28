Solution: B08 - FIND THE PROCESS

Concept  
Linux process management and CLI argument analysis.

Walkthrough  
1. Inspect `challenge/processes.txt`.
2. Locate the line for user `investigator`:
   `4192 investigator /opt/forensics/agent --inspect --token=investigator`
3. Extract PID `4192` and token `investigator`.
4. Assemble the flag: `flag{pid 4192 investigator}`.

Flag  
`flag{pid 4192 investigator}`
