n = int(input())
q = int(input())
a = [0] * n

for _ in range(q):
    k = int(input())
    a[k] += 1

print('\n'.join([str(x) for x in a]))
