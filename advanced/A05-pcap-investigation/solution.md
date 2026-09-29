# Solution: A05 - PCAP INVESTIGATION

## Concept
Multi-stream network forensics, protocol correlation, payload reconstruction across fragmented TCP sessions, and XOR stream decryption.

## Walkthrough
1. Inspect the packet capture (`challenge/capture.pcap`) using Wireshark, `tshark`, or the included script `python challenge/dissect_pcap.py`.
2. Observe multiple network conversations:
   - Client (`10.0.2.15`) communicating with HTTP C2 server (`198.51.100.88:80`).
   - Client communicating with internal intranet server (`10.0.2.1:80`).
   - Client sending raw TCP packets to (`198.51.100.88:8888`).
3. Follow the HTTP stream to `198.51.100.88:80`:
   - Inspect the HTTP response from the C2 server:
     ```http
     HTTP/1.1 200 OK
     X-Exfil-Key: 0x4B
     Content-Type: application/json

     {"status": "session_active", "exfil_port": 8888, "assembly_sequence": ["PART_1", "PART_2", "PART_3"]}
     ```
   - Key: `0x4B`
   - Sequence: `["PART_1", "PART_2", "PART_3"]`
4. Filter for port 8888 traffic:
   - Notice chunks arrive out-of-order:
     * Packet 4 contains: `[PART_2]:11190a0f0b4b`
     * Packet 5 contains: `[PART_1]:3b282a3b4b38`
     * Packet 6 contains: `[PART_3]:2e333f392a283f2e2f`
5. Assemble chunks in specified manifest order:
   - `PART_1`: `3b282a3b4b38`
   - `PART_2`: `11190a0f0b4b`
   - `PART_3`: `2e333f392a283f2e2f`
   - Combined hex: `3b282a3b4b3811190a0f0b4b2e333f392a283f2e2f`
6. XOR decrypt the assembled bytes with key `0x4B`:
   ```python
   raw = bytes.fromhex("3b282a3b4b3811190a0f0b4b2e333f392a283f2e2f")
   flag = "".join(chr(b ^ 0x4B) for b in raw)
   print(flag) # pcap stream extracted
   ```
7. Recover the flag: `pcap stream extracted`.

## Flag
`pcap stream extracted`
