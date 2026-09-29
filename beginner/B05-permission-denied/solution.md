# Solution: B05 - PERMISSION DENIED

## Concept
Linux access control uses file mode bits (rwx for User, Group, and Others). Files with world read permissions (such as mode 0644 `-rw-r--r--`) can be opened and inspected by non-root users.

## Walkthrough
1. Inspect file details in `challenge/audit/`:
   ```bash
   ls -l challenge/audit/
   ```
2. Check the permission modes of each entry:
   - `database.conf` (restricted)
   - `root_secret.key` (restricted)
   - `system_kernel.log` (restricted)
   - `public_report.txt` (`-rw-r--r--`, readable by others)
3. Read `public_report.txt`:
   ```bash
   cat challenge/audit/public_report.txt
   ```
4. Flag recovered:
   ```
   audit_permit_override_64
   ```

## Flag
`audit_permit_override_64`
