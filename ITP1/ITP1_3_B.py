import sys
i = 0
for line in sys.stdin:
    n = int(line)
    if 0 == n:
        break
    i += 1
    print(f'Case {i:d}: {n:d}')
