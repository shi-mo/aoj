import sys
import itertools

def gen_testcases(n: int):
    lp = list(itertools.permutations(range(1,n+1)))
    l = len(lp)
    for i in range(0,l):
        perm_id = "".join([str(x) for x in lp[i]])
        fname = f'_tc_n{n:d}_{perm_id}'
        with open(f'{fname:s}.in', 'w') as f:
            print(n, file=f)
            print(*(lp[i]), file=f)
        with open(f'{fname:s}.out', 'w') as f:
            if 0 < i: print(*(lp[i-1]), file=f)
            print(*(lp[i]), file=f)
            if i < (l-1): print(*(lp[i+1]), file=f)

n = int(sys.argv[1])
gen_testcases(n)
