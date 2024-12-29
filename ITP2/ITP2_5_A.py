n = int(input())
a = []

for i in range(0,n):
    x,y = [int(w) for w in input().split()]
    a.append([x,y])

for x,y in sorted(a):
    print(f'{x:d} {y:d}')
