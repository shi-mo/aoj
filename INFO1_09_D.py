n = int(input())
q = int(input())
a = [0] * n

for _ in range(q):
    l = int(input())
    r = int(input())
    for i in range(l,r+1): a[i] += 1

print('\n'.join([str(x) for x in a]))
