Solution: A06 - DNS EXFILTRATION

Concept  
DNS tunneling and chunked payload reassembly.

Walkthrough  
1. Filter the DNS logs for queries to `exfil.domain.com`:
   - 01: `666c61677b` ('flag{')
   - 02: `646e735f65` ('dns_e')
   - 03: `7866696c5f` ('xfil_')
   - 04: `6368756e6b` ('chunk')
   - 05: `5f72656173` ('_reas')
   - 06: `73656d626c` ('sembl')
   - 07: `65647d`     ('ed}')
2. Assemble the full hexadecimal string:
   `666c61677b646e735f657866696c5f6368756e6b5f7265617373656d626c65647d`
3. Decode to ASCII:
   `flag{dns_exfil_chunk_reassembled}`

Flag  
`flag{dns_exfil_chunk_reassembled}`
