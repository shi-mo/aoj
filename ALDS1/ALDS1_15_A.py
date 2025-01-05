n = int(input())
ans = 0
for d in [25, 10, 5, 1]:
    ans += n // d
    n %= d
print(ans)