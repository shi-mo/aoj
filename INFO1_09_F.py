n = int(input())
x = [int(input()) for _ in range(n)]

for a in sorted(set(x)):
    print(a)
