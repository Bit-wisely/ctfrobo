# Stego Chain decoder helper

import base64

def solve_chain(extracted_payload):
    print(f"Extracted payload: {extracted_payload}")
    # Decode base64
    decoded = base64.b64decode(extracted_payload).decode('utf-8')
    print(f"Decoded Flag: {decoded}")
    return decoded

if __name__ == '__main__':
    sample_payload = "ZmxhZ3tzdGVnb19jaGFpbl9kZWNvZGVkfQ=="
    solve_chain(sample_payload)
