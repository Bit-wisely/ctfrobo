# Hints: B08 - WHICH DOOR?

### Hint 1
Network administrators use standard port assignments below 1024 for essential Internet services. Look over the active listening services recorded in the scan.

### Hint 2
Plaintext HTTP traffic typically traverses port 80, but modern web applications enforce transport layer encryption (TLS/HTTPS) on another well-known default port.

### Hint 3
Locate the service entry dedicated to encrypted web communication in the port list and examine its service banner information.
