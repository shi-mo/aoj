x = int(input())

g = None
if   80 <= x: g = 'A'
elif 65 <= x: g = 'B'
elif 50 <= x: g = 'C'
elif 35 <= x: g = 'D'
else:         g = 'F'

print(g)
