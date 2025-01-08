from os.path import dirname, abspath
DIR = dirname(abspath(__file__))

S_LEN_MAX = 10 ** 5

with open(f'{DIR}/1-1.in', 'w', encoding='utf-8') as f:
    print('h'*S_LEN_MAX, file=f)

with open(f'{DIR}/1-1.out', 'w', encoding='utf-8') as f:
    print(S_LEN_MAX, file=f)

with open(f'{DIR}/1-2.in', 'w', encoding='utf-8') as f:
    print('hg'*(S_LEN_MAX//2), file=f)

with open(f'{DIR}/1-2.out', 'w', encoding='utf-8') as f:
    print(S_LEN_MAX, file=f)

with open(f'{DIR}/1-3.in', 'w', encoding='utf-8') as f:
    print('ghij'*(S_LEN_MAX//4), file=f)

with open(f'{DIR}/1-4.out', 'w', encoding='utf-8') as f:
    print(S_LEN_MAX*2, file=f)