n = int(input())
a = []

for i in range(0,n):
    l = input().split()
    v = int(l[0])
    w = int(l[1])
    t =     l[2]
    d = int(l[3])
    s =     l[4]
    a.append([v,w,t,d,s])

for v,w,t,d,s in sorted(a):
    print(f'{v:d} {w:d} {t:s} {d:d} {s:s}')
