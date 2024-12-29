x = int(input())

b32 = 0xffffffff
for a in [x, ~x, x<<1, x>>1]:
    print(format(a & b32, '032b'))
