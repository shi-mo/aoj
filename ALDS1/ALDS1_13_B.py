from heapq import heappush,heappop
from collections import defaultdict
import math

def main():
    v = ""
    for _ in range(3):
        for x in input().split():
            v += x
    print(dijkstra(v))

def dijkstra(start):
    goal = '123456780'
    cost_to = defaultdict(lambda: math.inf)
    cost_to[start] = 0
    heap = []
    heappush(heap, (0, start))
    heappush(heap, (math.inf, goal))
    while heap:
        cost, node = heappop(heap)
        if cost_to[node] < cost: continue

        for neighbor in neighbors_for(node):
            if neighbor != goal and math.inf == cost_to[neighbor]:
                cost_to[neighbor] = cost + 1
                heappush(heap, (cost+1, neighbor))
                continue
            cost_from_neighbor = cost_to[neighbor] + 1
            if cost_from_neighbor < cost:
                cost_to[node] = cost_from_neighbor
                heappush(heap, (cost_from_neighbor, node))
    return cost_to[goal]

def neighbors_for(nd):
    i0 = nd.index('0')
    l = []
    if 3 <= i0: # up
        l.append(str_swap(nd, i0-3, i0))
    if i0 < 6: # down
        l.append(str_swap(nd, i0, i0+3))
    if 0 < i0%3: # left
        l.append(str_swap(nd, i0-1, i0))
    if i0%3 < 2: # right
        l.append(str_swap(nd, i0, i0+1))
    return l

def str_swap(s, i, j):
    # assume i < j
    return s[:i] + s[j] + s[i+1:j] + s[i] + s[j+1:]
main()