from os.path import dirname, abspath
import random

DIR = dirname(abspath(__file__))

N_MAX = M_MAX = 100
V_MAX = 10 ** 4

with open(f'{DIR}/1-1.in', 'w', encoding='utf-8') as f:
    print('''\
1 1
0
''', end='', file=f)

with open(f'{DIR}/1-1.out', 'w', encoding='utf-8') as f:
    print('', end='', file=f)

with open(f'{DIR}/1-2.in', 'w', encoding='utf-8') as f:
    print('''\
1 1
0
0 0
''', end='', file=f)

with open(f'{DIR}/1-2.out', 'w', encoding='utf-8') as f:
    print('0', file=f)

with open(f'{DIR}/1-3.in', 'w', encoding='utf-8') as f:
    print(f'''\
1 1
{V_MAX}
0 0
''', end='', file=f)

with open(f'{DIR}/1-3.out', 'w', encoding='utf-8') as f:
    print(V_MAX, file=f)

with open(f'{DIR}/2-1.in', 'w', encoding='utf-8') as f:
    print(f'{N_MAX} {M_MAX}', file=f)
    random.seed(0)
    for i in range(N_MAX):
        for j in range(M_MAX):
            if 0 < j: print(' ', end='', file=f)
            print(random.randint(0, V_MAX), end='', file=f)
        print('', file=f)
    for i in range(N_MAX):
        for j in range(M_MAX):
            print(f'{i} {j}', file=f)

with open(f'{DIR}/2-1.out', 'w', encoding='utf-8') as f:
    random.seed(0)
    for i in range(N_MAX):
        for j in range(M_MAX):
            print(random.randint(0, V_MAX), file=f)