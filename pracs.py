# n3_5
def fast_mul(x, y):
    r = 0
    for i in range(0, y - 1):
        if y % 2 == 1:
            r += x
        x <<= 1
        y >>= 1
    return r


assert fast_mul(10, 15) == 150
assert fast_mul(0, 15) == 0
assert fast_mul(1, 15) == 15


# n3_6
def fast_pow(base, exponent):
    result = 1
    while exponent > 0:
        if exponent % 2 == 1:
            result *= base
        base *= base
        exponent >>= 1
    return result


assert fast_pow(2, 10) == 1024
assert fast_pow(2, 0) == 1
assert fast_pow(2, 1) == 2


# n3_7
def mul_bits(x, y, bits):
    x &= (2 ** bits - 1)
    y &= (2 ** bits - 1)
    return x * y


def mul16(x, y):
    x0 = x & 0xff
    x1 = x >> 8
    y0 = y & 0xff
    y1 = y >> 8

    p0 = mul_bits(x0, y0, 8)
    p1 = mul_bits(x1, y0, 8)
    p2 = mul_bits(x0, y1, 8)
    p3 = mul_bits(x1, y1, 8)

    return p0 + ((p1 + p2) << 8) + (p3 << 16)


assert mul16(10, 15) == 150
assert mul16(0, 15) == 0
assert mul16(1, 15) == 15


# n3_8
def mul16k(x, y):
    x0 = x & 0xff
    x1 = x >> 8
    y0 = y & 0xff
    y1 = y >> 8

    ac = x1 * y1
    bd = x0 * y0
    e = (x0 + x1) * (y0 + y1) - ac - bd

    return (ac << 16) + (e << 8) + bd


assert mul16k(10, 15) == 150
assert mul16k(0, 15) == 0
assert mul16k(1, 15) == 15


# n3_9
def fast_mul_gen(y):
    assignments = [f"y = x"]

    for i in range(1, y.bit_length() + 1):
        if y & 1:
            assignments.append(f"y += y")
        else:
            assignments.append(f"y += x")
        y >>= 1

    function_body = ["\n    " + str(i) for i in assignments]
    function_text = f"def f(x):{''.join(function_body)}\n    return y\n"
    return function_text


y = 12
x = 15
exec(fast_mul_gen(y), globals())

assert f(x) == x * y


def fast_mul_gen_pow(y):
    assignments = [f"y = x"]

    for i in range(1, y):
        assignments.append(f"y *= x")

    function_body = ["\n    " + str(i) for i in assignments]
    function_text = f"def f_pow(x):{''.join(function_body)}\n    return y\n"
    return function_text


exec(fast_mul_gen_pow(y), globals())

assert f_pow(x) == x ** y