# #1
# def func():
# 	if True:
#     	print("E101 indentation contains mixed spaces and tabs")
#
#
# def func():
#   print("E111 indentation is not a multiple of four")
#
#
# def func():
# print("E112 expected an indented block")
#
#
# var = some_function("string",
# "E121 continuation line under-indented for hanging indent")

#2
[0xfor _ in 'abc']

#2.2

a = 1
b = 1
c = 300000 # проверено в Python 3.11
d = 300000
print(a is b, c is d)


a, b = 'py', 'py'
c = ''.join(['p', 'y'])
print(a is b, a == c, a is c)

2.3

i = 'muchcodewow'
print(i[:4])
print(i[4:8])
print(i[8:11])



# #2.4
# lst = ['a', 'b', 'c']
# lst += 'd'
# print(lst)
#
# lst = lst + 'd' # Ошибка?!
# print(lst)
#
# lst += 42
# print(lst) # Ошибка?!

#3
s = ['1', '2', '3']
# s = ['apple', 'banana', 'cherry', 'apple']
x = 'apple'
n = 18

#3.1
print(list(map(int, s)))

#3.2
print(len(set(s)))

#3.3
print(s[::-1])

#3.4
print([i for i, v in enumerate(s) if v == x])

# #3.5
print(sum(int(s[i]) for i in range(len(s)) if i % 2 == 0))

#3.6
print(max(s, key=len))

#3.7
print((lambda n: n % sum(int(digit) for digit in str(n)) == 0)(18))

#3.8
import random, string; print(''.join(random.choices(string.ascii_letters + string.digits, k=10)))

#3.9
from itertools import groupby; rle_encode = lambda s: [(k, len(list(g))) for k, g in groupby(s)]
print(rle_encode('ABBCCCDEFFFFFFFFF'))



