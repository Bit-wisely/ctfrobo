Solution: A05 - PCAP INVESTIGATION

Concept  
Packet capture analysis and payload stream extraction.

Walkthrough  
1. Inspect the packet stream in `challenge/capture.pcap` using `strings`:
   ```bash
   strings challenge/capture.pcap | grep "flag{"
   ```
2. Or use `tcpdump -r challenge/capture.pcap -A`.
3. Locate the flag payload:
   `flag{pcap_stream_extracted}`

Flag  
`flag{pcap_stream_extracted}`
