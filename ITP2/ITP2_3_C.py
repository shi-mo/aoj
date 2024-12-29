import sys

_ = int(sys.stdin.readline())
a = [int(w) for w in sys.stdin.readline().split()]
q = int(sys.stdin.readline())

for i in range(0,q):
    b,e,k = [int(w) for w in sys.stdin.readline().split()]
    print(a[b:e].count(k))
