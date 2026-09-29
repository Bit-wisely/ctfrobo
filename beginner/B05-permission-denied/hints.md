# Hints: B05 - PERMISSION DENIED

### Hint 1
Execute the policy validator script (`verify_access.py`). Notice the exact error message and what permission mode it reports for the target credential file.

### Hint 2
In Unix/Linux security, tools like OpenSSH and GPG enforce the "Principle of Least Privilege": sensitive keys and credentials must not be readable or writable by other users or groups on the system.

### Hint 3
Review the octal numbering system used by `chmod`:
- Read (`r`) = 4
- Write (`w`) = 2
- Execute (`x`) = 1
Configure the file so that only the owner has read and write permissions (4 + 2 = 6), while group and others receive zero access (0).
