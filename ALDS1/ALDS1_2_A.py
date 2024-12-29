import sys

def bubble_sort(A: "List[int]"):
    n = len(A)
    nswap = 0
    for i in range(n):
        for j in reversed(range(i+1,n)):
            if A[j] < A[j-1]:
                temp = A[j]
                A[j] = A[j-1]
                A[j-1] = temp
                nswap += 1
    return nswap

N = int(sys.stdin.readline())
A = [int(w) for w in sys.stdin.readline().split()]
nswap = bubble_sort(A)
print(' '.join([str(ai) for ai in A]))
print(nswap)
