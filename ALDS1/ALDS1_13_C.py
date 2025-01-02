from heapq import heappush,heappop
from collections import defaultdict
from functools import total_ordering
import math

def main():
    v = ""
    for _ in range(4):
        for x in input().split():
            v += format(int(x), 'x')
    print(astar(v))

@total_ordering
class Node:
    instance_of = {}
    cost_of  = {}
    @classmethod
    def parse(cls, str, cost):
        return cls(str, cost)

    @classmethod
    def search(cls, str):
        if str not in cls.instance_of:
            return None
        return cls.instance_of[str]

    def __init__(self, str, cost):
        self.string = str
        self.vec = [int(c,16) for c in str]
        self.heuristic = self.md_for(self.vec)
        self.update_cost(cost)
    
    def update_cost(self, new_cost):
        new_score = new_cost + self.heuristic
        self.cost = new_cost
        self.score = new_score
        cls = self.__class__
        str = self.string
        cls.cost_of[str] = new_cost

    MANHATTAN_DISTANCE = [
        [ 6,0,1,2, 3,1,2,3, 4,2,3,4, 5,3,4,5 ],
        [ 5,1,0,1, 2,2,1,2, 3,3,2,3, 4,4,3,4 ],
        [ 4,2,1,0, 1,3,2,1, 2,4,3,2, 3,5,4,3 ],
        [ 3,3,2,1, 0,4,3,2, 1,5,4,3, 2,6,5,4 ],
        [ 5,1,2,3, 4,0,1,2, 3,1,2,3, 4,2,3,4 ],
        [ 4,2,1,2, 3,1,0,1, 2,2,1,2, 3,3,2,3 ],
        [ 3,3,2,1, 2,2,1,0, 1,3,2,1, 2,4,3,2 ],
        [ 2,4,3,2, 1,3,2,1, 0,4,3,2, 1,5,4,3 ],
        [ 4,2,3,4, 5,1,2,3, 4,0,1,2, 3,1,2,3 ],
        [ 3,3,2,3, 4,2,1,2, 3,1,0,1, 2,2,1,2 ],
        [ 2,4,3,2, 3,3,2,1, 2,2,1,0, 1,3,2,1 ],
        [ 1,5,4,3, 2,4,3,2, 1,3,2,1, 0,4,3,2 ],
        [ 3,3,4,5, 6,2,3,4, 5,1,2,3, 4,0,1,2 ],
        [ 2,4,3,4, 5,3,2,3, 4,2,1,2, 3,1,0,1 ],
        [ 1,5,4,3, 4,4,3,2, 3,3,2,1, 2,2,1,0 ],
        [ 0,6,5,4, 3,5,4,3, 2,4,3,2, 1,3,2,1 ]
    ]
    def md_for(self, vec):
        h = 0
        for i, vi in enumerate(vec):
            h += self.MANHATTAN_DISTANCE[i][vi]
        return h

    def neighbors(self):
        s = self.string
        i0 = s.index('0')
        ls = []
        if 4 <= i0: # up
            ls.append(self.str_swap(s, i0-4, i0))
        if i0 < 12: # down
            ls.append(self.str_swap(s, i0, i0+4))
        if 0 < i0%4: # left
            ls.append(self.str_swap(s, i0-1, i0))
        if i0%4 < 3: # right
            ls.append(self.str_swap(s, i0, i0+1))
        nbrs = []
        for s in ls:
            nbrs.append(Node.search(s) or Node.parse(s, math.inf))
        return nbrs

    def str_swap(self, s, i, j):
        # assume i < j
        return s[:i] + s[j] + s[i+1:j] + s[i] + s[j+1:]

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return NotImplemented
        return self.score == other.score \
            and self.cost == other.cost

    def __lt__(self, other):
        if not isinstance(other, self.__class__):
            return NotImplemented
        if self.score == other.score:
            return self.cost < other.cost
        return self.score < other.score

MAX_STEPS = 45
def astar(start):
    goal = '123456789abcdef0'
    heap = []
    heappush(heap, Node.parse(start, 0))
    heappush(heap, Node.parse(goal, math.inf))
    while heap and math.inf == Node.cost_of[goal]:
        node = heappop(heap)
        for nbr in node.neighbors():
            if math.inf == nbr.cost:
                nbr.update_cost(node.cost + 1)
                heappush(heap, nbr)
                continue

            score_node = node.score
            score_from_nbr = nbr.score + 1
            if score_node < score_from_nbr:
                continue
            if score_from_nbr < score_node:
                node.update_cost(nbr.cost + 1)
                continue
            if (nbr.cost + 1) < node.cost:
                node.update_cost(nbr.cost + 1)
    return Node.cost_of[goal]

main()