def encode_rle(data):
    encoded = bytearray()
    count = 1
    last_char = data[0]
    for i in range(1, len(data)):
        if data[i] == last_char:
            count += 1
        else:
            encoded.append(count)
            encoded.append(last_char)
            last_char = data[i]
            count = 1
    encoded.append(count)
    encoded.append(last_char)
    return bytes(encoded)

def decode_rle(data):
    decoded = bytearray()
    i = 0
    while i < len(data):
        count = data[i]
        char = data[i + 1]
        decoded.extend([char] * count)
        i += 2
    return bytes(decoded)
