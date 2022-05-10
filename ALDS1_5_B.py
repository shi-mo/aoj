import sys
import math

def merge(A, left: int, mid: int, right: int):
    n1 = mid - left
    n2 = right - mid
    L = A[left:left+n1] + [math.inf]
    R = A[mid :mid +n2] + [math.inf]

    i, j = 0, 0
    ncmp = 0
    for k in range(left,right):
        ncmp += 1
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
            continue
        A[k] = R[j]
        j += 1
    return ncmp

def merge_sort(A, left, right):
    if right <= left+1: return 0
    ncmp = 0
    mid = (left+right)//2
    ncmp += merge_sort(A, left, mid)
    ncmp += merge_sort(A, mid, right)
    ncmp += merge(A, left, mid, right)
    return ncmp

n = int(sys.stdin.readline())
S = [int(w) for w in sys.stdin.readline().split()]

ncmp = merge_sort(S, 0, n)
print(*S)
print(ncmp)
