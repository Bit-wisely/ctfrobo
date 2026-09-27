**A06 - DNS EXFILTRATION**

**Points**: 450  
**Category**: Advanced / DNS Tunneling  

**Challenge Overview**  
DNS tunneling is a technique used by adversaries to exfiltrate data from restricted corporate environments where direct HTTP/HTTPS outbound traffic is blocked by firewalls. By encoding pieces of confidential data into subdomains of recursive DNS lookups, the data reaches an attacker-controlled authoritative nameserver.

**Participant Question**  
DNS requests are everywhere. Most are boring. These aren't. Someone used the names being requested to carry something else.

**Clue**  
Extract the sequential hex fragments from subdomains querying `exfil.domain.com`. Assemble the fragments in index order (`01` through `07`) and decode to ASCII.

**Challenge Files**  
- `challenge/dns.log`

**Flag Format**  
`flag{...}`
