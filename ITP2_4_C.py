import sys

_ = int(sys.stdin.readline())
a = [int(w) for w in sys.stdin.readline().split()]
q = int(sys.stdin.readline())

for i in range(0,q):
    b,e,t = [int(w) for w in sys.stdin.readline().split()]
    a[b:e],a[t:t+(e-b)] = a[t:t+(e-b)],a[b:e]
print(*a)
