from collections import deque

n,q = [int(w) for w in input().split()]
queue = deque()
for i in range(n):
    name,time = input().split()
    queue.append([name,int(time)])

stamp = 0
while queue:
    name,time = queue.popleft()
    if time <= q:
        stamp += time
        print("{} {}".format(name,stamp))
        continue
    stamp += q
    queue.append([name,time-q])
