from os.path import dirname, abspath

DIR = dirname(abspath(__file__))
T_LEN_MAX = 1000
T_MAX = 'Z' * T_LEN_MAX

with open(f'{DIR}/corner1-1.in', 'w', encoding='utf-8') as f:
    print(T_MAX, file=f)
    print('Z', file=f)

with open(f'{DIR}/corner1-1.out', 'w', encoding='utf-8') as f:
    for i in range(T_LEN_MAX):
        print(i, file=f)

with open(f'{DIR}/corner1-2.in', 'w', encoding='utf-8') as f:
    print(T_MAX, file=f)
    print('ZZ', file=f)

with open(f'{DIR}/corner1-2.out', 'w', encoding='utf-8') as f:
    for i in range(T_LEN_MAX-1):
        print(i, file=f)

with open(f'{DIR}/corner1-3.in', 'w', encoding='utf-8') as f:
    print(T_MAX, file=f)
    print('ZZ', file=f)

with open(f'{DIR}/corner1-3.out', 'w', encoding='utf-8') as f:
    for i in range(T_LEN_MAX-1):
        print(i, file=f)

with open(f'{DIR}/corner2.in', 'w', encoding='utf-8') as f:
    print(T_MAX, file=f)
    print(T_MAX, file=f)

with open(f'{DIR}/corner2.out', 'w', encoding='utf-8') as f:
    print('0', file=f)

with open(f'{DIR}/corner3-1.in', 'w', encoding='utf-8') as f:
    print(T_MAX, file=f)
    print(T_MAX[:-1], file=f)

with open(f'{DIR}/corner3-1.out', 'w', encoding='utf-8') as f:
    print('0', file=f)
    print('1', file=f)

with open(f'{DIR}/corner3-2.in', 'w', encoding='utf-8') as f:
    print(T_MAX, file=f)
    print(T_MAX[:-1]+'a', file=f)

with open(f'{DIR}/corner3-2.out', 'w', encoding='utf-8') as f:
    print('', end='', file=f)

with open(f'{DIR}/corner3-3.in', 'w', encoding='utf-8') as f:
    print(T_MAX, file=f)
    print('a', file=f)

with open(f'{DIR}/corner3-3.out', 'w', encoding='utf-8') as f:
    print('', end='', file=f)

with open(f'{DIR}/corner4.in', 'w', encoding='utf-8') as f:
    print(T_MAX[:-1], file=f)
    print(T_MAX, file=f)

with open(f'{DIR}/corner4.out', 'w', encoding='utf-8') as f:
    print('', end='', file=f)
