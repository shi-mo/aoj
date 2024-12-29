from heapq import heappop,heappush
import sys

ans = []
h = []
for l in sys.stdin.readlines():
    if l.startswith('insert'):
        heappush(h, -int(l.split()[1]))
    elif l.startswith('extract'):
        ans.append(f'{(-heappop(h)):d}\n')
    else:
        break
sys.stdout.writelines(ans)
