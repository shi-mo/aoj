import sys

def is_prime(x: int):
    if 2 == x:
        return True
    if x < 2:
        return False
    if 0 == x%2:
        return False
    for i in range(3, int(x**0.5)+1, 2):
        if 0 == x%i:
            return False
    return True

_ = sys.stdin.readline()
ans = 0
for line in sys.stdin:
    x = int(line)
    ans += 1 if is_prime(x) else 0
print(ans)
