import base64

def solve_chain(extracted_payload):
    print(f"Extracted payload: {extracted_payload}")
    decoded = base64.b64decode(extracted_payload).decode('utf-8')
    print(f"Decoded Flag: {decoded}")
    return decoded

if __name__ == '__main__':
    sample_payload = "c3RlZ28gY2hhaW4gZGVjb2RlZA=="
    solve_chain(sample_payload)
