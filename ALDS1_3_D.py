import sys
from collections import deque

MAX_INPUT_LENGTH = 20_000
stack = deque()
finished = deque()
for _ in range(MAX_INPUT_LENGTH):
    c = sys.stdin.read(1)
    if not c or '\n' == c:
        break
    if c not in '/_\\':
        raise RuntimeError('Invalid input.')

    if '\\' == c:
        stack.append(('\\',0,0))
        continue
    if '_' == c:
        stack.append(('_',1,0))
        continue
    if '/' == c:
        length = 0
        area = 0
        lslash_found = False
        backup = deque()
        while stack:
            cp,l,a = stack.pop()
            if '\\' == cp:
                lslash_found = True
                break
            if '_' == cp:
                backup.append((cp,l,a))
                length += l
                area += a
            else:
                raise Exception('must not happen.')
        if not lslash_found:
            while backup:
                finished.append(backup.pop())
            continue
        stack.append(('_',length+2,area+length+1))
        continue
    raise Exception('must not happen.')

l = [area for c,l,area in (finished+stack) if '_' == c and 0 < area]
print(sum(l))
print(len(l), end=(' ' if 0 < len(l) else ''))
print(*l)
