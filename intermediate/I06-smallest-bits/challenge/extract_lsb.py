def extract_lsb_from_raw(raw_bytes):
    bits = []
    for b in raw_bytes:
        bits.append(str(b & 1))
    
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
    print("Example flag recovered from hidden bits: flag{lsb bits unlocked}")
