def main(r):
    s1 = set(r)
    for i in range(len(s)):
        if not (s[i] - s1):
            return i


s = ({'LESS', 1966, 1973, 'BRO'},
     {'LESS', 1966, 1973, 'HLSL'},
     {'LESS', 1966, 1973, 'LLVM'},
     {'LESS', 1966, 1922},
     {'LESS', 2015},
     {'MUF'},
     {'J', 1973, 'BRO'},
     {'J', 1973, 'HLSL', 1966},
     {'J', 1973, 'HLSL', 2015},
     {'J', 1973, 'LLVM', 1966},
     {'J', 1973, 'LLVM', 2015},
     {'J', 1922})

     # {x[0], x[1], x[2], x[3], x[4]}

print(main(['HLSL', 1973, 'MUF', 2015, 'YAML']),
main(['BRO', 1973, 'LESS', 2015, 'YAML']),
main(['LLVM', 1973, 'J', 2015, 'YAML']),
main(['LLVM', 1992, 'J', 1966, 'YAML']),
main(['LLVM', 1973, 'J', 1966, 'QML'])
)