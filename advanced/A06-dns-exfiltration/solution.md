Solution: A06 - DNS EXFILTRATION

Concept  
DNS tunneling and chunked payload reassembly.

Walkthrough  
1. Filter the DNS logs for queries to `exfil.domain.com`:
   - 01: `666c61677b` ('flag{')
   - 02: `646e732065` ('dns e')
   - 03: `7866696c20` ('xfil ')
   - 04: `6368756e6b` ('chunk')
   - 05: `2072656173` (' reas')
   - 06: `73656d626c` ('sembl')
   - 07: `65647d`     ('ed}')
2. Assemble the full hexadecimal string:
   `666c61677b646e7320657866696c206368756e6b207265617373656d626c65647d`
3. Decode to ASCII:
   `flag{dns exfil chunk reassembled}`

Flag  
`flag{dns exfil chunk reassembled}`
