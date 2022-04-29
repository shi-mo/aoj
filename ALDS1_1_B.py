import sys

def gcd(x: int, y: int):
    x, y = max(x,y), min(x,y)
    while 0 < y:
        m = x % y
        x, y = max(y,m), min(y,m)
    return x

x, y = [int(w) for w in sys.stdin.readline().split()]
print(gcd(x, y))
