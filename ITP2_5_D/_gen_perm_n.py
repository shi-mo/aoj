import sys
import itertools

def gen_testcases(n: int):
    fname = f'_tc_n{n:d}'
    with open(f'{fname:s}.in', 'w') as f:
        print(n, file=f)
    with open(f'{fname:s}.out', 'w') as f:
        for p in itertools.permutations(range(1,n+1)):
            print(*p, file=f)

n = int(sys.argv[1])
gen_testcases(n)
