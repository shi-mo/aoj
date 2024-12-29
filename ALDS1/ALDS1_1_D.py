import sys

n = int(sys.stdin.readline())

ans = -1000000000
rmin = int(sys.stdin.readline())
for line in sys.stdin:
    r = int(line)
    rd = r - rmin
    if ans < rd:
        ans = rd
    if r < rmin:
        rmin = r
print(ans)
