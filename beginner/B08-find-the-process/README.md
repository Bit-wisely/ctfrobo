**B08 - FIND THE PROCESS**

**Points**: 200  
**Category**: Beginner / Linux Processes  

**Challenge Overview**  
Modern multi-user systems run hundreds of concurrent background processes. Incident responders and system administrators must be able to inspect process listings to detect anomalous behaviors, unauthorized binaries, or misplaced credentials left on the command line.

**Participant Question**  
Hundreds of things may be running. Only one of them belongs to the investigator. Find it.

**Clue**  
Filter the process list by the `investigator` username and extract both the PID and the secret token parameter.

**Challenge Files**  
- `challenge/processes.txt`

**Flag Format**  
`flag{pid_<PID>_<SECRET_KEY>}`
