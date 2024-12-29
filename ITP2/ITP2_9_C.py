_ = input()
a = set([int(x) for x in input().split()])
_ = input()
b = set([int(x) for x in input().split()])

for v in sorted(list(a - b)):
    print(v)
