import struct
from enum import Enum


class Types(Enum):
    uint8 = '<B'
    uint16 = '<H'
    uint32 = '<I'
    uint64 = '<Q'
    int8 = '<b'
    int16 = '<h'
    int32 = '<i'
    int64 = '<q'
    float = '<f'
    double = '<d'
    char = '<c'


class BinaryReader:
    def __init__(self, source, offset):
        self.source = source
        self.offset = offset

    def read(self, pattern):
        value = struct.unpack_from(pattern.value, self.source, self.offset)
        self.offset += struct.calcsize(pattern.value)
        return value[0]


def read_a(reader: BinaryReader):
    a1 = reader.read(Types.int8)
    a2 = read_b(reader)
    a3 = reader.read(Types.uint8)
    a4 = reader.read(Types.int16)
    a5 = []
    for i in range(5):
        a5.append(read_e(BinaryReader
                         (reader.source, reader.read(Types.uint32))))
    a6_size = reader.read(Types.uint32)
    a6_address = reader.read(Types.uint32)
    a6_reader = BinaryReader(reader.source, a6_address)
    a6 = []
    for _ in range(a6_size):
        a6.append(a6_reader.read(Types.int32))
    return dict(A1=a1, A2=a2, A3=a3, A4=a4, A5=a5, A6=a6)


def read_b(reader: BinaryReader):
    b1 = read_c(BinaryReader(reader.source, reader.read(Types.uint32)))
    b2 = reader.read(Types.uint32)
    b3 = read_d(reader)
    b4 = reader.read(Types.uint16)
    b5 = reader.read(Types.double)
    b6 = reader.read(Types.int32)
    b7 = reader.read(Types.int64)
    return dict(B1=b1, B2=b2, B3=b3, B4=b4, B5=b5, B6=b6, B7=b7)


def read_c(reader: BinaryReader):
    c1 = reader.read(Types.double)
    c2 = reader.read(Types.int8)
    c3_size = reader.read(Types.uint16)
    c3_address = reader.read(Types.uint32)
    c3_reader = BinaryReader(reader.source, c3_address)
    c3 = ''.join([chr(c3_reader.read(Types.uint8)) for _ in range(c3_size)])
    c4 = reader.read(Types.uint16)
    c5 = reader.read(Types.uint64)
    c6 = reader.read(Types.float)
    c7 = reader.read(Types.uint8)
    c8 = [reader.read(Types.uint16) for _ in range(2)]
    return dict(C1=c1, C2=c2, C3=c3, C4=c4, C5=c5, C6=c6, C7=c7, C8=c8)


def read_d(reader: BinaryReader):
    d1 = reader.read(Types.float)
    d2 = reader.read(Types.uint64)
    d3 = reader.read(Types.int16)
    d4 = reader.read(Types.double)
    d5 = reader.read(Types.float)
    d6 = reader.read(Types.int32)
    d7 = reader.read(Types.int16)
    d8 = reader.read(Types.uint8)
    return dict(D1=d1, D2=d2, D3=d3, D4=d4, D5=d5, D6=d6, D7=d7, D8=d8)


def read_e(reader: BinaryReader):
    e1 = reader.read(Types.int8)
    e2 = reader.read(Types.uint16)
    return dict(E1=e1, E2=e2)


def main(data):
    reader = BinaryReader(data, offset=5)  # Сигнатура занимает 5 байт
    return read_a(reader)


print(main(b'DCKV\xb9<g\x00\x00\x002e/C\xf1gB?\x1b1M\xd1.#\xb1Oi\xc5\xba\xacm\xe9'
           b'.F\xec\xbf)s\x97\xbeY\xdc\xa0\x9b\xcf\xa00({DD\xec\x8aa\xc1\xe1?=\xd6\xf7'
           b'\xd3\x88\x80\x99\x1a\xa9Q\xf0\x14\xfe\x9d\xea\x89\x00\x00\x00'
           b'\x8c\x00\x00\x00\x8f\x00\x00\x00\x92\x00\x00\x00\x95\x00\x00\x00'
           b'\x03\x00\x00\x00\x98\x00\x00\x00cma\x94\x05P@\xe4\x8f\xec\xbf\x03'
           b'\x03\x00d\x00\x00\x00\x07\xef\x10@\x00L\xc5\xcb\x0c\x122\xden?,g\x95Y/&7C'
           b')\xabu\x1e\x8c,\xa3\r\xc3\xf6h!W\xd7\x9dV\x83\xc99\x067\x89\xea\xb2'))

print(main(b'DCKV\xb9mf\x00\x00\x00\x14w\xea$*T6?\xe7\xd2\x93g"\xca\xeav1\xb1'
           b'6\x13\xdf\x86\x06\t\xe8?\x0c\xfc1\xbf\xd1&\xf9,\xeb S\xa8\xa2\xea\xd7 '
           b'\x90\r\x07\xe6?\x8dEsP^\xe4\x93pA`~\x1fUD:\x88\x00\x00\x00\x8b\x00\x00\x00'
           b'\x8e\x00\x00\x00\x91\x00\x00\x00\x94\x00\x00\x00\x05\x00\x00\x00'
           b'\x97\x00\x00\x00fc\xbc\x8b\xe4\x8fA\x9a\xe1?\xaa\x02\x00d\x00\x00'
           b'\x00"\xb3\x95kii<\\\xf4\xd7t\xeab>\x1e\x0fJ\xe6\x7f\t\x98<\xa2\xba\x11~\xdb'
           b'm\xe3Px\x89U\xda\t\xd8TA\xbc\xc2\x04\x9bh\xe5y\xd5\xde\x17\xd1\xa8(\x9bv!'))
