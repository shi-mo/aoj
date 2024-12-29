import sys

def selection_sort(A: "List[int]"):
    n = len(A)
    nswap = 0
    for i in range(n):
        minj = i
        for j in range(i, n):
            if A[j] < A[minj]:
                minj = j
        if minj != i:
            temp = A[i]
            A[i] = A[minj]
            A[minj] = temp
            nswap += 1
    return nswap

_ = int(sys.stdin.readline())
A = [int(w) for w in sys.stdin.readline().split()]
nswap = selection_sort(A)
print(' '.join([str(ai) for ai in A]))
print(nswap)
