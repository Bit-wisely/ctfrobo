Network packet dump collected from gateway switch.
Filter by UDP / TCP packets and search for ASCII text streams.
To analyze:
- Wireshark: Open capture.pcap -> filter by `frame contains "flag"`
- Strings: strings capture.pcap | grep "flag{"
