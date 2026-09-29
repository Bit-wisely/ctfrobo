# Solution: B08 - WHICH DOOR?

## Concept
Standard Internet networking services utilize well-known TCP port numbers assigned by IANA. While unencrypted HTTP runs over port 80, secure HTTPS (HTTP over TLS) is assigned to port 443.

## Walkthrough
1. Inspect `challenge/ports.txt`:
   ```bash
   cat challenge/ports.txt
   ```
2. Locate the service row corresponding to HTTPS:
   ```
   443/tcp    open  https      Apache/2.4.52 (TLSv1.3: port_443_tls_secure)
   ```
3. Extract the service flag token embedded in the banner:
   ```
   port_443_tls_secure
   ```

## Flag
`port_443_tls_secure`
