from os.path import dirname, abspath
DIR = dirname(abspath(__file__))

N_MAX = 10 ** 5
Q_MAX = 2 * (10 ** 5)
V_MAX = 10 ** 4

with open(f'{DIR}/1-1.in', 'w', encoding='utf-8') as f:
    print('''\
2 1
1 0 1
''', end='', file=f)

with open(f'{DIR}/1-1.out', 'w', encoding='utf-8') as f:
    print('?', file=f)

with open(f'{DIR}/1-2.in', 'w', encoding='utf-8') as f:
    print(f'''\
2 2
0 0 1 {V_MAX}
1 0 1
''', end='', file=f)

with open(f'{DIR}/1-2.out', 'w', encoding='utf-8') as f:
    print(V_MAX, file=f)

with open(f'{DIR}/2-1.in', 'w', encoding='utf-8') as f:
    print(f'{N_MAX} {Q_MAX}', file=f)
    for i in range(N_MAX):
        for j in range(Q_MAX//N_MAX):
            print(f'1 {i} {(i+j+1) % N_MAX}', file=f)

with open(f'{DIR}/2-1.out', 'w', encoding='utf-8') as f:
    for i in range(Q_MAX):
        print('?', file=f)

with open(f'{DIR}/2-2.in', 'w', encoding='utf-8') as f:
    print(f'{N_MAX} {2*(N_MAX-1)}', file=f)
    for i in range(N_MAX-1):
        print(f'0 {i} {i+1} 1', file=f)
    for i in range(1, N_MAX):
        print(f'1 0 {i}', file=f)

with open(f'{DIR}/2-2.out', 'w', encoding='utf-8') as f:
    for i in range(1, N_MAX):
        print(i, file=f)

with open(f'{DIR}/2-3.in', 'w', encoding='utf-8') as f:
    print(f'{N_MAX} {(N_MAX//2)-1 + (N_MAX-1)}', file=f)
    for i in range((N_MAX//2)-1):
        print(f'0 {2*i} {2*i+2} 2', file=f)
    for j in range(1, N_MAX):
        print(f'1 0 {j}', file=f)

with open(f'{DIR}/2-3.out', 'w', encoding='utf-8') as f:
    for j in range(1, N_MAX):
        print(j if 0 == j%2 else '?', file=f)

with open(f'{DIR}/2-4.in', 'w', encoding='utf-8') as f:
    print(f'{N_MAX} {2*N_MAX-4}', file=f)
    for i in range(N_MAX-2):
        print(f'0 {i} {i+2} 2', file=f)
    for j in range(2, N_MAX):
        print(f'1 1 {j}', file=f)

with open(f'{DIR}/2-4.out', 'w', encoding='utf-8') as f:
    for j in range(2, N_MAX):
        print(j-1 if 0 != j%2 else '?', file=f)