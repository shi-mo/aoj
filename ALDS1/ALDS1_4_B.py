import sys
import bisect

def binary_search(s: "List[int]", x: int):
    i = bisect.bisect_left(s, x)
    if i != len(s) and s[i] == x:
        return i
    raise ValueError

n = int(sys.stdin.readline())
s = [int(x) for x in sys.stdin.readline().split()]
q = int(sys.stdin.readline())
t = [int(x) for x in sys.stdin.readline().split()]

count = 0
for x in set(t):
    try:
        binary_search(s, x)
        count += 1
    except ValueError:
        pass
print(count)
