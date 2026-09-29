# Solution: B09 - FIND THE SERVER

## Concept
IPv4 Classless Inter-Domain Routing (CIDR) notation `/24` designates that the first 24 bits (three octets) constitute the network prefix. Correlating DNS hostnames with subnet definitions enables tracing target nodes in network logs.

## Walkthrough
1. Inspect `challenge/clues.txt`:
   - Target hostname: `vault.internal`
   - Target subnet: `192.168.10.0/24`
2. Inspect `challenge/network.txt`:
   ```
   vault.internal      52:54:00:12:34:56  192.168.10.45
   ```
3. Confirm that `192.168.10.45` is inside the `192.168.10.0/24` subnet.
4. Format the final flag as instructed:
   ```
   host_vault_192_168_10_45
   ```

## Flag
`host_vault_192_168_10_45`
