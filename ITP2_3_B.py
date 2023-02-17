import sys

_ = int(sys.stdin.readline())
a = [int(w) for w in sys.stdin.readline().split()]
q = int(sys.stdin.readline())

for i in range(0,q):
    c,b,e = [int(w) for w in sys.stdin.readline().split()]
    print(min(a[b:e]) if c < 1 else max(a[b:e]))
