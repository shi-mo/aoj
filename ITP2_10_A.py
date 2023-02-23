x = int(input())

b32 = 0xffffffff
print(format(x & b32, '032b'))
print(format(~x & b32, '032b'))
print(format(x<<1 & b32, '032b'))
print(format(x>>1 & b32, '032b'))
