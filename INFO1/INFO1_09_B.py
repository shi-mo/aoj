n = int(input())
a = [input() for _ in range(n)]
l = int(input())
r = int(input())

print('\n'.join(a[l:r+1]))
