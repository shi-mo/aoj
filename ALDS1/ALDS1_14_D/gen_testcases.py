from os.path import dirname, abspath
import random
import string

random.seed(1)
DIR = dirname(abspath(__file__))

T_LEN_MAX = 1000000
P_LEN_MAX = 1000
NUM_QUERIES_MAX = 10000

S = string.digits + string.ascii_letters

with open(f'{DIR}/1-1.in', 'w', encoding='utf-8') as f:
    t = ''.join(random.choices(S, k=NUM_QUERIES_MAX))
    tail = t[(-1)*P_LEN_MAX:]
    print(t, file=f)
    print(NUM_QUERIES_MAX, file=f)
    for i in range(NUM_QUERIES_MAX//2):
        print(tail, file=f)
        print(tail[:-1]+'0', file=f)

with open(f'{DIR}/1-1.out', 'w', encoding='utf-8') as f:
    for i in range(NUM_QUERIES_MAX//2):
        print('1', file=f)
        print('0', file=f)

with open(f'{DIR}/2-1.in', 'w', encoding='utf-8') as f:
    t = '0' * T_LEN_MAX
    print(t, file=f)
    print(NUM_QUERIES_MAX, file=f)
    for i in range(NUM_QUERIES_MAX):
        print('0', file=f)

with open(f'{DIR}/2-1.out', 'w', encoding='utf-8') as f:
    for i in range(NUM_QUERIES_MAX):
        print('1', file=f)

with open(f'{DIR}/3-1.in', 'w', encoding='utf-8') as f:
    print('''\
Z
1
Z
''', end='', file=f)

with open(f'{DIR}/3-1.out', 'w', encoding='utf-8') as f:
    print('1', file=f)

with open(f'{DIR}/3-2.in', 'w', encoding='utf-8') as f:
    print('''\
Z
1
a
''', end='', file=f)

with open(f'{DIR}/3-2.out', 'w', encoding='utf-8') as f:
    print('0', file=f)

with open(f'{DIR}/3-3.in', 'w', encoding='utf-8') as f:
    print('''\
a
1
a1
''', end='', file=f)

with open(f'{DIR}/3-3.out', 'w', encoding='utf-8') as f:
    print('0', file=f)

with open(f'{DIR}/3-4.in', 'w', encoding='utf-8') as f:
    print('''\
a
1
a{'1' * (P_LEN_MAX-1)}
''', end='', file=f)

with open(f'{DIR}/3-4.out', 'w', encoding='utf-8') as f:
    print('0', file=f)

with open(f'{DIR}/3-5.in', 'w', encoding='utf-8') as f:
    t = ''.join(random.choices(S, k=NUM_QUERIES_MAX))
    tail = t[(-1)*P_LEN_MAX:]
    print(f'''\
{tail[:-1]}
1
{tail}
''', end='', file=f)

with open(f'{DIR}/3-5.out', 'w', encoding='utf-8') as f:
    print('0', file=f)