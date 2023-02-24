n = int(input())

c = 0
for _ in range(n):
    a = int(input())
    if 0 == a:
        print(c)
        c = 0
        continue
    c += 1
