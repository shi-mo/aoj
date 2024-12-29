n = int(input())

a,b = [],[]
for _ in range(2*n):
    x = input()
    if '-' == x[0]: a.append(x)
    else: b.append(x)

for i in range(n):
    print(a[i], b[i])
