import sys

_ = int(sys.stdin.readline())
a = [int(w) for w in sys.stdin.readline().split()]
q = int(sys.stdin.readline())

for i in range(0,q):
    b,m,e = [int(w) for w in sys.stdin.readline().split()]
    a[b:e] = a[m:e] + a[b:m]
print(*a)
