a,b = [int(x) for x in input().split()]

b32 = 0xffffffff
for x in [a&b, a|b, a^b]:
    print(format(x & b32, '032b'))
