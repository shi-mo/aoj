print('(')
for i in range(16):
    r = i // 4
    c = i % 4
    adj = []
    if 0 < r: adj.append(i-4)
    if 0 < c: adj.append(i-1)
    if c < 3: adj.append(i+1)
    if r < 3: adj.append(i+4)
    print('    (', end='')
    for j, a in enumerate(adj):
        print(f'{a}', end='')
        if j < len(adj)-1: print(', ', end='')
    print(')', end='')
    if i < 15: print(',', end='')
    print('')
print(')')