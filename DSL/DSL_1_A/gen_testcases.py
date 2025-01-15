from os.path import dirname, abspath
DIR = dirname(abspath(__file__))

N_MAX = 10 ** 4
Q_MAX = 10 ** 5

with open(f'{DIR}/1-1.in', 'w', encoding='utf-8') as f:
    print('''\
2 1
1 0 1
''', end='', file=f)

with open(f'{DIR}/1-1.out', 'w', encoding='utf-8') as f:
    print('0', file=f)

with open(f'{DIR}/1-2.in', 'w', encoding='utf-8') as f:
    print('''\
2 2
0 0 1
1 0 1
''', end='', file=f)

with open(f'{DIR}/1-2.out', 'w', encoding='utf-8') as f:
    print('1', file=f)

with open(f'{DIR}/2-1.in', 'w', encoding='utf-8') as f:
    print(f'{N_MAX} {Q_MAX}', file=f)
    for i in range(N_MAX):
        for j in range(Q_MAX//N_MAX):
            print(f'1 {i} {(i+j+1) % N_MAX}', file=f)

with open(f'{DIR}/2-1.out', 'w', encoding='utf-8') as f:
    for i in range(Q_MAX):
        print('0', file=f)

with open(f'{DIR}/2-2.in', 'w', encoding='utf-8') as f:
    print(f'{N_MAX} {Q_MAX}', file=f)
    for i in range(N_MAX-1):
        print(f'0 {i} {i+1}', file=f)
    print(f'0 {N_MAX-1} {0}', file=f)
    for i in range(N_MAX-1):
        for j in range(Q_MAX//N_MAX):
            print(f'1 {i} {(i+j+1) % N_MAX}', file=f)

with open(f'{DIR}/2-2.out', 'w', encoding='utf-8') as f:
    for i in range(Q_MAX-N_MAX):
        print('1', file=f)

with open(f'{DIR}/2-3.in', 'w', encoding='utf-8') as f:
    print(f'{N_MAX} {Q_MAX}', file=f)
    for _ in range(2):
        for i in range((N_MAX//2)-1):
            print(f'0 {2*i} {2*i+2}', file=f)
        print(f'0 {N_MAX-2} {0}', file=f)
    for x in range(Q_MAX-N_MAX):
        i = x // (Q_MAX//N_MAX)
        j = x % (Q_MAX//N_MAX)
        print(f'1 {i} {(i+j+1) % N_MAX}', file=f)

with open(f'{DIR}/2-3.out', 'w', encoding='utf-8') as f:
    for x in range(Q_MAX-N_MAX):
        i = x // (Q_MAX//N_MAX)
        j = x % (Q_MAX//N_MAX)
        print('1' if 0 == i%2 and 0 == (j+1)%2 else '0', file=f)

with open(f'{DIR}/2-4.in', 'w', encoding='utf-8') as f:
    print(f'{N_MAX} {Q_MAX}', file=f)
    for i in range(N_MAX-2):
        print(f'0 {i} {i+2}', file=f)
    print(f'0 {N_MAX-2} 0', file=f)
    print(f'0 {N_MAX-1} 1', file=f)
    for x in range(Q_MAX-N_MAX):
        i = x // (Q_MAX//N_MAX)
        j = x % (Q_MAX//N_MAX)
        print(f'1 {i} {(i+j+1) % N_MAX}', file=f)

with open(f'{DIR}/2-4.out', 'w', encoding='utf-8') as f:
    for x in range(Q_MAX-N_MAX):
        i = x // (Q_MAX//N_MAX)
        j = x % (Q_MAX//N_MAX)
        print('1' if i%2 == (i+j+1)%2 else '0', file=f)