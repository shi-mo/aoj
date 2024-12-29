import sys
import math
from collections import deque

RT3 = math.sqrt(3)

def koch(n,p,q):
    if 0 == n: return deque()

    global RT3
    x1, y1 = p
    x2, y2 = q
    dx, dy = (x2-x1), (y2-y1)
    dx3, dy3 = dx/3, dy/3
    s = (x1+dx3, y1+dy3)
    t = (x1+(2*dx3), y1+(2*dy3))
    v, w = (dx/2)-((dy/2)/RT3), (dy/2)+((dx/2)/RT3)
    u = (x1+v, y1+w)

    result = deque()
    result += koch(n-1,p,s)
    result.append(s)
    result += koch(n-1,s,u)
    result.append(u)
    result += koch(n-1,u,t)
    result.append(t)
    result += koch(n-1,t,q)
    return result

n = int(input())
p = (0.0, 0.0)
q = (100.0, 0.0)
answer = deque()
answer.append(p)
answer += koch(n,p,q)
answer.append(q)
for pos in answer:
    if not pos: continue
    x, y = pos
    print(f'{x:.8f} {y:.8f}')
