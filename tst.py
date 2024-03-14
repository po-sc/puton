#1.1
import math

res = 4.2e1
res = 0o52
res = 0x2a
res = 0b101010
res = 42
res = 420e-1
res = 42.00


assert res == 42


#1.2
huge_int = 2 ** 10000


max_float = 1.7976931348623157e+308
print(max_float)

overflow_float = max_float * 2
print(overflow_float)


#1.5
z = 1
z <<= 5
result = 2 ** z
print(result)



#1.6
i = 0
while i < 10:
    print(i)
    i += 1




#1.7
print((True * 2 + False) * -True)




#1.8
x = 5
1 < x < 10
# True

x = 5
1 < (x < 10)
# False




#3.1
def mul_12(a):
    b = a
    a = a + a
    b = a + a
    b = a + b
    return b + b
mul_12 (1)




#3.2
def mul_16(x):
    x = x + x
    x = x + x
    x = x + x
    return x + x
mul_16 (1)


#3.3
def mul_15(a):
    b = a + a
    b = b + b
    b = b + b
    c = a - b
    return b - c
mul_15 (1)




#3.5
def fast_mul(a, b):
    c = 0
    while b > 0:
        if b & 1:
            c += a
        a <<= 1
        b >>= 1
    return c

print(fast_mul(10, 15))


#3.6
def fast_pow(b, e):
    r = 1
    while e > 0:
        if e & 1:
            r = fast_mul(r, b)
        b = fast_mul(b, b)
        e >>= 1
    return r


def test_fast_pow():
    assert fast_pow(2, 3) == 8, "PRESS F"
test_fast_pow()

print(fast_pow(2, 5))