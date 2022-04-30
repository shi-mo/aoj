import copy
import sys

def card(w):
    return {'suit': w[0], 'value': int(w[1])}

def bubble_sort(A: "List[int]"):
    n = len(A)
    for i in range(n):
        for j in reversed(range(i+1,n)):
            if A[j]['value'] < A[j-1]['value']:
                temp = A[j]
                A[j] = A[j-1]
                A[j-1] = temp

def selection_sort(A: "List[int]"):
    n = len(A)
    for i in range(n):
        minj = i
        for j in range(i, n):
            if A[j]['value'] < A[minj]['value']:
                minj = j
        if minj != i:
            temp = A[i]
            A[i] = A[minj]
            A[minj] = temp

N = int(sys.stdin.readline())
A = [card(w) for w in sys.stdin.readline().split()]
A1 = copy.deepcopy(A)
A2 = copy.deepcopy(A)
A.sort(key = lambda ai: ai['value'])

bubble_sort(A1)
print(' '.join([ai['suit']+str(ai['value']) for ai in A1]))
print('Stable' if A1 == A else 'Not stable')

selection_sort(A2)
print(' '.join([ai['suit']+str(ai['value']) for ai in A2]))
print('Stable' if A2 == A else 'Not stable')
