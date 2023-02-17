import sys

n = int(sys.stdin.readline())
a = [int(w) for w in sys.stdin.readline().split()]
m = int(sys.stdin.readline())
b = [int(w) for w in sys.stdin.readline().split()]

for i in range(0,min(n,m)):
    if a[i] == b[i]: continue
    print(1 if a[i] < b[i] else 0)
    sys.exit(0)
print(1 if n < m else 0)
