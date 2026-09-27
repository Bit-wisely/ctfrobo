**A05 - PCAP INVESTIGATION**

**Points**: 400  
**Category**: Advanced / Network Forensics  

**Challenge Overview**  
Network packet captures (.pcap files) record full Ethernet frames and higher-layer protocols traversing a network segment. Packet analysis tools allow security analysts to inspect network sessions, identify suspicious hosts, and reconstruct unencrypted data payloads.

**Participant Question**  
You weren't watching the network when it happened. Fortunately, someone captured the traffic. Find what shouldn't be there.

**Clue**  
Open `capture.pcap` with a packet analyzer (such as Wireshark or `tcpdump`) and inspect the payload stream within the UDP packets.

**Challenge Files**  
- `challenge/capture.pcap`
- `challenge/README.txt`

**Flag Format**  
`flag{...}`
