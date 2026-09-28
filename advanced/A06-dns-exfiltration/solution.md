# Solution: A06 - DNS EXFILTRATION

## Concept
DNS tunneling and chunked payload reassembly.

## Walkthrough
1. Filter the DNS logs for queries to `exfil.domain.com`:
   - 01: `646e732065` ('dns e')
   - 02: `7866696c20` ('xfil ')
   - 03: `6368756e6b` ('chunk')
   - 04: `2072656173` (' reas')
   - 05: `73656d626c` ('sembl')
   - 06: `6564`       ('ed')
2. Assemble the full hexadecimal string:
   `646e7320657866696c206368756e6b207265617373656d626c6564`
3. Decode to ASCII:
   `dns exfil chunk reassembled`

## Flag
`dns exfil chunk reassembled`
