import sys
import math

def step_insertion_sort(A: "List[int]", g: int):
    n = len(A)
    cnt = 0
    for i in range(g,n):
        v = A[i]
        j = i - g
        while 0 <= j and v < A[j]:
            A[j+g] = A[j]
            j -= g
            cnt += 1
        A[j+g] = v
    return cnt

def primes_3to(root_n: int):
    limit = root_n + 1
    is_prime = None
    if 0 == limit%2:
        is_prime = [False,True] * int(limit/2)
    else:
        is_prime = ([False,True] * int(limit/2)) + [False]

    is_prime[0] = False
    is_prime[1] = False

    for i in range(3,int(root_n**0.5)+1,2):
        if not is_prime[i]:
            continue
        for j in range(2*i,limit,i):
            is_prime[j] = False

    is_prime[2] = False # eliminate 2 (for this problem)
    return [p for p in range(limit) if is_prime[p]]

def shell_sort(A: "List[int]"):
    n = len(A)
    cnt = 0
    G = [2**i for i in reversed(range(int(math.log2(n))))]
    m = len(G)
    for gi in G:
         cnt += step_insertion_sort(A, gi)
    return [m,G,cnt]

_ = sys.stdin.readline()
A = [int(line) for line in sys.stdin]

m,G,cnt = shell_sort(A)
print(m)
print(' '.join([str(gi) for gi in G]))
print(cnt)
for ai in A:
    print(ai)
