# Solution: A05 - PCAP INVESTIGATION

## Concept
Packet capture analysis and payload stream extraction.

## Walkthrough
1. Inspect the packet stream in `challenge/capture.pcap` using `strings`:
   ```bash
   strings challenge/capture.pcap | grep "pcap stream extracted"
   ```
2. Or use `tcpdump -r challenge/capture.pcap -A`.
3. Locate the flag payload:
   `pcap stream extracted`

## Flag
`pcap stream extracted`
