Solution: B06 - THE LOST FILE

Concept
Recursive filesystem search and directory traversal using command-line utilities.

Walkthrough
1. Explore the lost_files directory using directory listing commands:
   ls
2. When the directory tree becomes too broad or deeply nested, perform a recursive file search:
   find . -type f
3. Locate the target file nested inside the backup hierarchy at backups/backup2/old/notes/final/meeting_notes.txt.
4. Read the contents of the target file:
   cat backups/backup2/old/notes/final/meeting_notes.txt
5. The file contains the message with the final answer: blue-screen.

Flag
blue-screen
