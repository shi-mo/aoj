from os.path import dirname, abspath

DIR = dirname(abspath(__file__))
H_MAX = W_MAX = 1000
R_MAX = C_MAX = 1000

with open(f'{DIR}/1-1.in', 'w', encoding='utf-8') as f:
    print('''\
1 1
a
1 1
a
''' , end='', file=f)

with open(f'{DIR}/1-1.out', 'w', encoding='utf-8') as f:
    print('0 0', file=f)

with open(f'{DIR}/1-2.in', 'w', encoding='utf-8') as f:
    print('''\
1 1
a
1 1
b
''' , end='', file=f)

with open(f'{DIR}/1-2.out', 'w', encoding='utf-8') as f:
    pass

with open(f'{DIR}/1-3.in', 'w', encoding='utf-8') as f:
    print('''\
1 1
a
1 2
ab
''' , end='', file=f)

with open(f'{DIR}/1-3.out', 'w', encoding='utf-8') as f:
    pass

with open(f'{DIR}/1-4.in', 'w', encoding='utf-8') as f:
    print('''\
1 1
a
2 1
a
b
''' , end='', file=f)

with open(f'{DIR}/1-4.out', 'w', encoding='utf-8') as f:
    pass

with open(f'{DIR}/1-5.in', 'w', encoding='utf-8') as f:
    print('''\
2 2
aa
aa
1 1
a
''' , end='', file=f)

with open(f'{DIR}/1-5.out', 'w', encoding='utf-8') as f:
    print('''\
0 0
0 1
1 0
1 1
''' , end='', file=f)

with open(f'{DIR}/1-6.in', 'w', encoding='utf-8') as f:
    print('''\
3 3
aaa
aaa
aaa
2 2
aa
aa
''' , end='', file=f)

with open(f'{DIR}/1-6.out', 'w', encoding='utf-8') as f:
    print('''\
0 0
0 1
1 0
1 1
''' , end='', file=f)

with open(f'{DIR}/2-1.in', 'w', encoding='utf-8') as f:
    print(f'''\
{H_MAX} {W_MAX}
{('Z'*W_MAX + '\n') * H_MAX}\
{R_MAX} {C_MAX}
{('Z'*C_MAX + '\n') * R_MAX}\
''' , end='', file=f)

with open(f'{DIR}/2-1.out', 'w', encoding='utf-8') as f:
    print('0 0', file=f)

with open(f'{DIR}/2-2.in', 'w', encoding='utf-8') as f:
    print(f'''\
{H_MAX} {W_MAX}
{('Z'*W_MAX + '\n') * H_MAX}\
{R_MAX} {C_MAX}
{(('Z'*C_MAX + '\n') * (R_MAX-1)) + ('Z'*(C_MAX-1) + 'a\n')}\
''' , end='', file=f)

with open(f'{DIR}/2-2.out', 'w', encoding='utf-8') as f:
    pass

with open(f'{DIR}/2-3.in', 'w', encoding='utf-8') as f:
    print(f'''\
{H_MAX-1} {W_MAX}
{('Z'*W_MAX + '\n') * (H_MAX-1)}\
{R_MAX} {C_MAX}
{('Z'*C_MAX + '\n') * R_MAX}\
''' , end='', file=f)

with open(f'{DIR}/2-3.out', 'w', encoding='utf-8') as f:
    pass

with open(f'{DIR}/2-4.in', 'w', encoding='utf-8') as f:
    print(f'''\
{H_MAX} {W_MAX-1}
{('Z'*(W_MAX-1) + '\n') * H_MAX}\
{R_MAX} {C_MAX}
{('Z'*C_MAX + '\n') * R_MAX}\
''' , end='', file=f)

with open(f'{DIR}/2-4.out', 'w', encoding='utf-8') as f:
    pass

with open(f'{DIR}/3-1.in', 'w', encoding='utf-8') as f:
    print(f'''\
{H_MAX} {W_MAX}
{('Z'*W_MAX + '\n') * H_MAX}\
{R_MAX-1} {C_MAX-1}
{('Z'*(C_MAX-1) + '\n') * (R_MAX-1)}\
''' , end='', file=f)

with open(f'{DIR}/3-1.out', 'w', encoding='utf-8') as f:
    for i in range(2):
        for j in range(2):
            print(f'{i} {j}', file=f)

with open(f'{DIR}/3-2.in', 'w', encoding='utf-8') as f:
    print(f'''\
{H_MAX} {W_MAX}
{('Z'*W_MAX + '\n') * H_MAX}\
{R_MAX-1} {C_MAX}
{('Z'*C_MAX + '\n') * (R_MAX-1)}\
''' , end='', file=f)

with open(f'{DIR}/3-2.out', 'w', encoding='utf-8') as f:
    for i in range(2):
        print(f'{i} 0', file=f)

with open(f'{DIR}/3-3.in', 'w', encoding='utf-8') as f:
    print(f'''\
{H_MAX} {W_MAX}
{('Z'*W_MAX + '\n') * H_MAX}\
{R_MAX} {C_MAX-1}
{('Z'*(C_MAX-1) + '\n') * R_MAX}\
''' , end='', file=f)

with open(f'{DIR}/3-3.out', 'w', encoding='utf-8') as f:
    for j in range(2):
        print(f'0 {j}', file=f)

with open(f'{DIR}/3-4.in', 'w', encoding='utf-8') as f:
    print(f'''\
{H_MAX} {W_MAX}
{('Z'*W_MAX + '\n') * H_MAX}\
2 2
ZZ
ZZ
''' , end='', file=f)

with open(f'{DIR}/3-4.out', 'w', encoding='utf-8') as f:
    for i in range(H_MAX-1):
        for j in range(W_MAX-1):
            print(f'{i} {j}', file=f)

with open(f'{DIR}/3-5.in', 'w', encoding='utf-8') as f:
    print(f'''\
{H_MAX} {W_MAX}
{('Z'*W_MAX + '\n') * H_MAX}\
1 1
Z
''' , end='', file=f)

with open(f'{DIR}/3-5.out', 'w', encoding='utf-8') as f:
    for i in range(H_MAX):
        for j in range(W_MAX):
            print(f'{i} {j}', file=f)

with open(f'{DIR}/3-6.in', 'w', encoding='utf-8') as f:
    print(f'''\
{H_MAX} {W_MAX}
{('Z'*W_MAX + '\n') * H_MAX}\
1 1
0
''' , end='', file=f)

with open(f'{DIR}/3-6.out', 'w', encoding='utf-8') as f:
    pass

with open(f'{DIR}/3-7.in', 'w', encoding='utf-8') as f:
    print(f'''\
{H_MAX} {W_MAX}
{('Z'*W_MAX + '\n') * H_MAX}\
2 2
ZZ
Zz
''' , end='', file=f)

with open(f'{DIR}/3-7.out', 'w', encoding='utf-8') as f:
    pass

with open(f'{DIR}/3-8.in', 'w', encoding='utf-8') as f:
    n = 30
    print(f'''\
{H_MAX} {W_MAX}
{('0'*W_MAX + '\n') * H_MAX}\
{n} {n}
{('0'*n + '\n') * n}\
''' , end='', file=f)

with open(f'{DIR}/3-8.out', 'w', encoding='utf-8') as f:
    n = 30
    for i in range(H_MAX-n+1):
        for j in range(H_MAX-n+1):
            print(f'{i} {j}', file=f)

with open(f'{DIR}/3-9.in', 'w', encoding='utf-8') as f:
    n = 100
    print(f'''\
{H_MAX} {W_MAX}
{('0'*W_MAX + '\n') * H_MAX}\
{n} {n}
{('0'*n + '\n') * n}\
''' , end='', file=f)

with open(f'{DIR}/3-9.out', 'w', encoding='utf-8') as f:
    n = 100
    for i in range(H_MAX-n+1):
        for j in range(H_MAX-n+1):
            print(f'{i} {j}', file=f)

with open(f'{DIR}/3-10.in', 'w', encoding='utf-8') as f:
    n = 500
    print(f'''\
{H_MAX} {W_MAX}
{('0'*W_MAX + '\n') * H_MAX}\
{n} {n}
{('0'*n + '\n') * n}\
''' , end='', file=f)

with open(f'{DIR}/3-10.out', 'w', encoding='utf-8') as f:
    n = 500
    for i in range(H_MAX-n+1):
        for j in range(H_MAX-n+1):
            print(f'{i} {j}', file=f)

with open(f'{DIR}/4-1.in', 'w', encoding='utf-8') as f:
    print(f'''\
{H_MAX} {W_MAX}
{('Za'*(W_MAX//2) + '\n') * H_MAX}\
{R_MAX} {C_MAX}
{('Za'*(C_MAX//2) + '\n') * R_MAX}\
''' , end='', file=f)

with open(f'{DIR}/4-1.out', 'w', encoding='utf-8') as f:
    print('0 0', file=f)

with open(f'{DIR}/4-2.in', 'w', encoding='utf-8') as f:
    print(f'''\
{H_MAX} {W_MAX}
{('Za'*(W_MAX//2) + '\n') * H_MAX}\
1 {C_MAX}
{('Za'*(C_MAX//2) + '\n')}\
''' , end='', file=f)

with open(f'{DIR}/4-2.out', 'w', encoding='utf-8') as f:
    for i in range(H_MAX):
        print(f'{i} 0', file=f)

with open(f'{DIR}/4-3.in', 'w', encoding='utf-8') as f:
    print(f'''\
{H_MAX} {W_MAX}
{('Za'*(W_MAX//2) + '\n') * H_MAX}\
{R_MAX} 2
{'Za\n'*R_MAX}\
''' , end='', file=f)

with open(f'{DIR}/4-3.out', 'w', encoding='utf-8') as f:
    for j in range(W_MAX//2):
        print(f'0 {j*2}', file=f)

with open(f'{DIR}/4-4.in', 'w', encoding='utf-8') as f:
    print(f'''\
{H_MAX} {W_MAX}
{(('Za'*(W_MAX//2) + '\n') + ('aZ'*(W_MAX//2) + '\n')) * (H_MAX//2)}\
2 2
Za
aZ
''' , end='', file=f)

with open(f'{DIR}/4-4.out', 'w', encoding='utf-8') as f:
    for i in range(H_MAX):
        for j in range(W_MAX):
            if i%2 == j%2 and i < H_MAX-1 and j < W_MAX-1:
                print(f'{i} {j}', file=f)

with open(f'{DIR}/4-5.in', 'w', encoding='utf-8') as f:
    import string
    s1 = string.digits + string.ascii_letters
    n = len(s1)
    m = W_MAX // n
    s2 = s1 * m
    w = len(s2)
    print(f'''\
{H_MAX} {w}
{(s2 + '\n') * H_MAX}\
{m} {n}
{(s1 + '\n') * m}\
''' , end='', file=f)

with open(f'{DIR}/4-5.out', 'w', encoding='utf-8') as f:
    for i in range(H_MAX-m+1):
        for j in range(m):
            print(f'{i} {j*n}', file=f)