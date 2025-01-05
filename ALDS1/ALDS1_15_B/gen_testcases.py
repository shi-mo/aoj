from os.path import dirname, abspath
DIR = dirname(abspath(__file__))

N_MAX = 10 ** 5
W_MAX = 10 ** 9
V_MAX = 10 ** 9

with open(f'{DIR}/1-1.in', 'w', encoding='utf-8') as f:
    print(f'{N_MAX} {W_MAX}', file=f)
    for i in range(N_MAX):
        print(f'{V_MAX} {W_MAX}', file=f)

with open(f'{DIR}/1-1.out', 'w', encoding='utf-8') as f:
    print(f'{V_MAX}', file=f)

with open(f'{DIR}/1-2.in', 'w', encoding='utf-8') as f:
    print(f'{N_MAX} {W_MAX}', file=f)
    for i in range(N_MAX):
        print(f'{V_MAX} 1', file=f)

with open(f'{DIR}/1-2.out', 'w', encoding='utf-8') as f:
    print(f'{V_MAX * N_MAX}', file=f)

with open(f'{DIR}/2-1.in', 'w', encoding='utf-8') as f:
    print(f'''\
1 1
1 3
''', end='', file=f)

with open(f'{DIR}/2-1.out', 'w', encoding='utf-8') as f:
    print('0.33333333', file=f)

with open(f'{DIR}/2-2.in', 'w', encoding='utf-8') as f:
    print(f'''\
1 {W_MAX-1}
{V_MAX} {W_MAX}
''', end='', file=f)

with open(f'{DIR}/2-2.out', 'w', encoding='utf-8') as f:
    print(W_MAX-1, file=f)

with open(f'{DIR}/2-3.in', 'w', encoding='utf-8') as f:
    print(f'''\
1 {W_MAX//2}
{V_MAX} {W_MAX}
''', end='', file=f)

with open(f'{DIR}/2-3.out', 'w', encoding='utf-8') as f:
    print(V_MAX//2, file=f)

with open(f'{DIR}/2-4.in', 'w', encoding='utf-8') as f:
    print(f'''\
1 {W_MAX//3}
{V_MAX} {W_MAX}
''', end='', file=f)

with open(f'{DIR}/2-4.out', 'w', encoding='utf-8') as f:
    print(V_MAX//3, file=f)

with open(f'{DIR}/2-5.in', 'w', encoding='utf-8') as f:
    print(f'''\
1 3
{V_MAX} 9
''', end='', file=f)

with open(f'{DIR}/2-5.out', 'w', encoding='utf-8') as f:
    print('333333333.33333331', file=f)