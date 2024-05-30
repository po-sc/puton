import pytest
from rle import encode_rle, decode_rle

@pytest.fixture
def sample_data():
    return b"aaabbbccddddd"

@pytest.mark.parametrize("input_data, expected", [
    (b"aaabbbccddddd", b"\x03a\x03b\x02c\x05d"),
    (b"", b""),
    (b"a", b"\x01a"),
    (b"ab", b"\x01a\x01b")
])
def test_encode_rle(input_data, expected):
    assert encode_rle(input_data) == expected

@pytest.mark.parametrize("input_data, expected", [
    (b"\x03a\x03b\x02c\x05d", b"aaabbbccddddd"),
    (b"", b""),
    (b"\x01a", b"a"),
    (b"\x01a\x01b", b"ab")
])
def test_decode_rle(input_data, expected):
    assert decode_rle(input_data) == expected

def test_encode_decode(sample_data):
    encoded = encode_rle(sample_data)
    decoded = decode_rle(encoded)
    assert decoded == sample_data

if __name__ == "__main__":
    pytest.main()
