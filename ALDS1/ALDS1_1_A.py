import sys

n = int(sys.stdin.readline())
a = [int(w) for w in sys.stdin.readline().split()]

print(' '.join([str(ai) for ai in a]))
for i in range(1,n):
    key = a[i]
    j = i - 1
    while 0 <= j and key < a[j]:
        a[j+1] = a[j]
        j -= 1
    a[j+1] = key
    print(' '.join([str(ai) for ai in a]))
