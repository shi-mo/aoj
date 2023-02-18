import sys

_ = int(sys.stdin.readline())
a = [int(w) for w in sys.stdin.readline().split()]

print(*list(dict.fromkeys(a)))
