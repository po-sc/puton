# x = 4
# y = 1
# print(((y & 7) + (x << (y if y >= 5 else 5))) - ((x * 3) if x >= (y // 5) else (y // 5)))


x = 4
y = 4
result = ((y if y > 1 else 3) + (x if y >= x else 10)) - y
print(result)



# #tree
# x=2
# y=2
# print(((x+(y>>6))+(y<<2 if x>=4 else 4))-y)


