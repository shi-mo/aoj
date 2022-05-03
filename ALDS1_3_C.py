import sys
from collections import deque

n = int(input())
queue = deque()
for i in range(n):
    line = sys.stdin.readline()
    command = None
    key = None
    if ' ' in line:
        command,x = line.split()
        key = int(x)
    else:
        command = line.rstrip()

    if 'insert' == command:
        queue.appendleft(key)
        continue
    if 'delete' == command:
        try:
            queue.remove(key)
        except ValueError:
            pass
        continue
    if 'deleteFirst' == command:
        queue.popleft()
        continue
    if 'deleteLast' == command:
        queue.pop()
        continue
    print('Error')
    break
print(*queue)
