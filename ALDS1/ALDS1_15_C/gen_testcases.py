from os.path import dirname, abspath
DIR = dirname(abspath(__file__))

N_MAX = 10 ** 5
T_MAX = 10 ** 9

with open(f'{DIR}/1-1.in', 'w', encoding='utf-8') as f:
    print(f'''\
1
1 2
''', end='', file=f)

with open(f'{DIR}/1-1.out', 'w', encoding='utf-8') as f:
    print('1', file=f)

with open(f'{DIR}/1-2.in', 'w', encoding='utf-8') as f:
    print(f'''\
1
1 {T_MAX}
''', end='', file=f)

with open(f'{DIR}/1-2.out', 'w', encoding='utf-8') as f:
    print('1', file=f)

with open(f'{DIR}/2-1.in', 'w', encoding='utf-8') as f:
    print(f'{N_MAX}', file=f)
    for i in range(1, N_MAX+1):
        print(f'{i} {i+1}', file=f)

with open(f'{DIR}/2-1.out', 'w', encoding='utf-8') as f:
    print(f'{N_MAX//2}', file=f)

with open(f'{DIR}/2-2.in', 'w', encoding='utf-8') as f:
    print(f'{N_MAX}', file=f)
    print(f'1 3', file=f)
    for i in range(1, N_MAX):
        print(f'{i} {i+1}', file=f)

with open(f'{DIR}/2-2.out', 'w', encoding='utf-8') as f:
    print(f'{N_MAX//2}', file=f)

with open(f'{DIR}/2-3.in', 'w', encoding='utf-8') as f:
    print(f'{N_MAX}', file=f)
    for i in range(N_MAX):
        print(f'1 2', file=f)

with open(f'{DIR}/2-3.out', 'w', encoding='utf-8') as f:
    print('1', file=f)

with open(f'{DIR}/2-4.in', 'w', encoding='utf-8') as f:
    print(f'{N_MAX}', file=f)
    for i in range(1, N_MAX+1):
        print(f'{2*i} {2*i+1}', file=f)

with open(f'{DIR}/2-4.out', 'w', encoding='utf-8') as f:
    print(f'{N_MAX}', file=f)

with open(f'{DIR}/2-5.in', 'w', encoding='utf-8') as f:
    print(f'{N_MAX}', file=f)
    for i in range(1, N_MAX+1):
        print(f'{i} {N_MAX+i+1}', file=f)

with open(f'{DIR}/2-5.out', 'w', encoding='utf-8') as f:
    print('1', file=f)

with open(f'{DIR}/2-6.in', 'w', encoding='utf-8') as f:
    print(f'{N_MAX}', file=f)
    for i in range(1, N_MAX+1):
        print(f'{i} {N_MAX+i-2}', file=f)

with open(f'{DIR}/2-6.out', 'w', encoding='utf-8') as f:
    print('2', file=f)

with open(f'{DIR}/2-7.in', 'w', encoding='utf-8') as f:
    print(f'{N_MAX}', file=f)
    for i in reversed(range(1, N_MAX+1)):
        print(f'{2*i} {2*i+1}', file=f)

with open(f'{DIR}/2-7.out', 'w', encoding='utf-8') as f:
    print(f'{N_MAX}', file=f)

with open(f'{DIR}/3-1.in', 'w', encoding='utf-8') as f:
    print(f'{N_MAX}', file=f)
    N2 = N_MAX//2
    for i in range(1, N2+1):
        print(f'{2*i} {2*i+1}', file=f)
    for i in range(1, N2+1):
        print(f'{N_MAX+i} {2*N_MAX}', file=f)

with open(f'{DIR}/3-1.out', 'w', encoding='utf-8') as f:
    print(f'{(N_MAX//2)+1}', file=f)