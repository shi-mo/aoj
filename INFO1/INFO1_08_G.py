n = int(input())
t = int(input())

s = 0
for _ in range(n):
    s += int(input())
    if s < t: continue
    print(s)
    break
