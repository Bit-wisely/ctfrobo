Hints: A05 - PCAP INVESTIGATION

1. Inspect the packet capture using `strings capture.pcap` or `tcpdump -r capture.pcap -X`.
2. Locate the UDP packet frames exchanged between the client and gateway.
3. The second UDP frame payload contains the cleartext flag string.
