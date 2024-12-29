import sys

def counting_sort(A, B, vmax):
    cnt = [0]*(vmax+1)
    for aj in A:
        cnt[aj] += 1

    for i in range(1,vmax):
        cnt[i] += cnt[i-1]
    for aj in reversed(A):
        B[cnt[aj]-1] = aj
        cnt[aj] -= 1

def main():
    n = int(input())
    A = list(map(int, sys.stdin.readline().split()))
    Amax = 2000000
    B = [None]*n
    counting_sort(A, B, Amax)
    print(*B)

main()
