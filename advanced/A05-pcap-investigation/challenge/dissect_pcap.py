#!/usr/bin/env python3
"""
PCAP Forensic Dissector Utility
Parses and correlates network streams in capture.pcap
"""
import struct
import os
import sys

def parse_pcap(filepath):
    if not os.path.exists(filepath):
        print(f"[-] PCAP file not found: {filepath}")
        return []
    
    packets = []
    with open(filepath, 'rb') as f:
        global_hdr = f.read(24)
        if len(global_hdr) < 24:
            return []
        
        pkt_num = 1
        while True:
            pkt_hdr = f.read(16)
            if len(pkt_hdr) < 16:
                break
            ts_sec, ts_usec, incl_len, orig_len = struct.unpack('<IIII', pkt_hdr)
            data = f.read(incl_len)
            
            # Ethernet (14) + IP (20)
            if len(data) >= 34:
                eth_type = struct.unpack('!H', data[12:14])[0]
                if eth_type == 0x0800: # IPv4
                    ip_hdr = data[14:34]
                    proto = ip_hdr[9]
                    src_ip = ".".join(str(b) for b in ip_hdr[12:16])
                    dst_ip = ".".join(str(b) for b in ip_hdr[16:20])
                    
                    if proto == 6 and len(data) >= 54: # TCP
                        tcp_hdr = data[34:54]
                        src_port, dst_port = struct.unpack('!HH', tcp_hdr[0:4])
                        payload = data[54:]
                        packets.append({
                            'num': pkt_num,
                            'src': f"{src_ip}:{src_port}",
                            'dst': f"{dst_ip}:{dst_port}",
                            'payload': payload
                        })
            pkt_num += 1
    return packets

def main():
    print("=" * 60)
    print("        DEEP PACKET FORENSICS DISSECTOR")
    print("              Target: capture.pcap")
    print("=" * 60)
    
    pcap_file = os.path.join(os.path.dirname(__file__), "capture.pcap")
    pkts = parse_pcap(pcap_file)
    print(f"\n[+] Loaded {len(pkts)} packets from capture.pcap:\n")
    
    for p in pkts:
        print(f"Packet #{p['num']}: {p['src']} -> {p['dst']} ({len(p['payload'])} bytes payload)")
        preview = p['payload'].decode('latin-1', errors='replace').strip()
        if preview:
            first_line = preview.splitlines()[0]
            print(f"   Preview: {first_line[:70]}")
    
    print("\n" + "=" * 60)
    print("Investigation Helper:")
    print("1. Inspect HTTP C2 Handshake on port 80 to find decryption key & chunk manifest.")
    print("2. Correlate with custom exfiltration channel on port 8888.")
    print("3. Reassemble chunks in sequence and XOR decrypt to recover the exfiltrated flag.")
    print("=" * 60 + "\n")

if __name__ == "__main__":
    main()
