a,b,c,d = [input() for _ in range(4)]
print(1 if (a == b and c == d) or (a == c and b == d) else 0)
