Network packet capture (capture.pcap) collected from perimeter monitoring TAP.
Investigate the concurrent sessions between the compromised host (10.0.2.15) and external infrastructure.

Tools for analysis:
- Wireshark: Open capture.pcap -> Follow TCP Streams
- TShark: tshark -r capture.pcap -Y "http || tcp.port == 8888" -T fields -e text
- Python: python dissect_pcap.py
