Solution: B07 - HIDDEN IN PLAIN SIGHT

Concept
Recognizing and discovering hidden directories and dotfiles in Linux filesystems.

Walkthrough
1. Inspect the case directory using the standard directory listing command:
   ls
2. Notice that ordinary listing hides dotfiles and hidden directories.
3. List all files including hidden entries:
   ls -la
4. Discover the hidden directory .hidden/.
5. Navigate into the hidden directory and list its contents:
   cd .hidden
   ls
6. Read the message file:
   cat message.txt
7. The file contains the final answer: Search me.

Flag
Search me
