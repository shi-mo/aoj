import sys

_ = int(sys.stdin.readline())
a = [int(w) for w in sys.stdin.readline().split()]
_ = int(sys.stdin.readline())
b = [int(w) for w in sys.stdin.readline().split()]

print(1 if a < b else 0)
