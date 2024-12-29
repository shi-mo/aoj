import itertools

n = int(input())

for p in itertools.permutations(range(1,n+1)):
    print(*p)
