from os.path import dirname, abspath
import random

DIR = dirname(abspath(__file__))

N_MAX = M_MAX = 100
Q_MAX = 10 ** 4

with open(f'{DIR}/1-1.in', 'w', encoding='utf-8') as f:
    print('''\
1 1 1
0 0
''', end='', file=f)

with open(f'{DIR}/1-1.out', 'w', encoding='utf-8') as f:
    print('1', file=f)

with open(f'{DIR}/1-2.in', 'w', encoding='utf-8') as f:
    print(f'''\
2 2 2
0 0
1 1
''', end='', file=f)

with open(f'{DIR}/1-2.out', 'w', encoding='utf-8') as f:
    print(f'''\
1 0
0 1
''', end='', file=f)

with open(f'{DIR}/1-3.in', 'w', encoding='utf-8') as f:
    print('''\
1 1 2
0 0
0 0
''', end='', file=f)

with open(f'{DIR}/1-3.out', 'w', encoding='utf-8') as f:
    print(0, file=f)

with open(f'{DIR}/2-1.in', 'w', encoding='utf-8') as f:
    print(f'{N_MAX} {M_MAX} {Q_MAX}', file=f)
    for i in range(N_MAX):
        for j in range(M_MAX):
            print(f'{i} {j}', file=f)

with open(f'{DIR}/2-1.out', 'w', encoding='utf-8') as f:
    for i in range(N_MAX):
        for j in range(M_MAX):
            if 0 < j: print(' ', end='', file=f)
            print(1, end='', file=f)
        print('', file=f)

with open(f'{DIR}/2-2.in', 'w', encoding='utf-8') as f:
    print(f'{N_MAX} {M_MAX} {N_MAX}', file=f)
    for i in range(N_MAX):
        print(f'{i} {i}', file=f)

with open(f'{DIR}/2-2.out', 'w', encoding='utf-8') as f:
    for i in range(N_MAX):
        for j in range(M_MAX):
            if 0 < j: print(' ', end='', file=f)
            print(1 if i == j else 0, end='', file=f)
        print('', file=f)

with open(f'{DIR}/2-3.in', 'w', encoding='utf-8') as f:
    print(f'{N_MAX} {M_MAX} {Q_MAX-N_MAX}', file=f)
    for i in range(N_MAX):
        for j in range(M_MAX):
            if i != j: print(f'{i} {j}', file=f)

with open(f'{DIR}/2-3.out', 'w', encoding='utf-8') as f:
    for i in range(N_MAX):
        for j in range(M_MAX):
            if 0 < j: print(' ', end='', file=f)
            print(1 if i != j else 0, end='', file=f)
        print('', file=f)

with open(f'{DIR}/2-4.in', 'w', encoding='utf-8') as f:
    print(f'{N_MAX} {M_MAX} {Q_MAX//2}', file=f)
    for i in range(N_MAX):
        for j in range(M_MAX):
            if i%2 == j%2: print(f'{i} {j}', file=f)

with open(f'{DIR}/2-4.out', 'w', encoding='utf-8') as f:
    for i in range(N_MAX):
        for j in range(M_MAX):
            if 0 < j: print(' ', end='', file=f)
            print(1 if i%2 == j%2 else 0, end='', file=f)
        print('', file=f)