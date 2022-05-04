import sys

n = int(sys.stdin.readline())
s = [int(x) for x in sys.stdin.readline().split()]
q = int(sys.stdin.readline())
t = [int(x) for x in sys.stdin.readline().split()]

in_s = {}
for x in s:
    in_s[x] = True

count = 0
for x in set(t):
    if x in in_s: count += 1
print(count)
