n = int(input())
for i in range(1, n+1):
    print(' '.join(['%d' % (i+int(x)) for x in input().split()]))
