def main(x):
    x = int(x)
    i1 = x & 0b1
    i2 = x & (0b111111111 << 1)
    i3 = x & (0b111 << 10)

    i1 <<= 17
    i2 <<= 2
    i3 >>= 10

    # return i1 + i2 + i3
    return f'{i1 + i2 + i3}'
    return f"'{result}'"

print(main('1426'))  # '1609'
print(main('610'))  # '2440'
print(main('6890'))  # '2990'
print(main('3741'))  # '133747'


#
# def main(x):
#     x = int(x)
#     i1 = x & 0b1
#     i2 = x & (0b111111111 << 1)
#     i3 = x & (0b111 << 10)
#
#     i1 <<= 17
#     i2 <<= 2
#     i3 >>= 10
#
#     result = i1 + i2 + i3
#     return f"'{result}'"
#
# print(main('1426'))  # '1609'
# print(main('610'))  # '2440'
# print(main('6890'))  # '2990'
# print(main('3741'))  # '133747'
