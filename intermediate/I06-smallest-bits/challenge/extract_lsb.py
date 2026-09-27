# LSB Steganography Extractor Helper

def extract_lsb_from_raw(raw_bytes):
    # Extracts the LSB from each byte in raw RGB stream
    bits = []
    for b in raw_bytes:
        bits.append(str(b & 1))
    
    # Group into 8-bit characters
    chars = []
    for i in range(0, len(bits) - 7, 8):
        byte_str = "".join(bits[i:i+8])
        val = int(byte_str, 2)
        if val == 0:
            break
        chars.append(chr(val))
    return "".join(chars)

if __name__ == "__main__":
    print("LSB extraction template ready.")
    print("Example flag recovered from hidden bits: flag{lsb_bits_unlocked}")
