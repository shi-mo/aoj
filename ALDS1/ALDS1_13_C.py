from heapq import heappush,heappop
import math

def main():
    print(astar(load_start_id()))

def load_start_id():
    v = []
    for _ in range(4):
        for x in input().split():
            v.append(int(x))
    return id_for(v)

# Convert list(int) into 64bit int
def id_for(vec):
    # assume len(vec) == 16 and 0 <= vec[i] < 16
    nd = 0
    for v in vec:
        nd = (nd << 4) | v
    return nd

def astar(start):
    MAX_COST = 45
    goal = int('123456789abcdef0', 16)
    visited = set()
    heap = []
    # node: (score, heuristic(MD), id, i0)
    heappush(heap, init_node_for(start))
    while heap:
        score, h, id, i0 = heappop(heap)
        cost = score - h
        if id in visited: continue
        if id == goal: return cost

        visited.add(id)
        for next_cell in ADJ_CELL_FOR[i0]:
            next_id = adj_id_for(id, i0, next_cell)
            if next_id in visited: continue

            lbl = label_at(i0, next_id)
            next_h = h + MD[i0][lbl] - MD[next_cell][lbl]
            next_cost = cost + 1
            if MAX_COST < next_cost: continue

            next_score = next_cost + next_h
            heappush(heap, (next_score, next_h, next_id, next_cell))
    return 'NO ANSWER'

ADJ_CELL_FOR = (
    (1,4),    (0,2,5),     (1,3,6),     (2,7),
    (0,5,8),  (1,4,6,9),   (2,5,7,10),  (3,6,11),
    (4,9,12), (5,8,10,13), (6,9,11,14), (7,10,15),
    (8,13),   (9,12,14),   (10,13,15),  (11,14)
)

def init_node_for(id):
    h = 0
    i0 = 0
    for i in range(16):
        lbl = label_at(i, id)
        if 0 < lbl: h += MD[i][lbl] # MUST NOT add MD for 0 (blank cell)
        if 0 == lbl: i0 = i
    return (h, h, id, i0)

MD = ( # manhattan distance
    ( 6,0,1,2, 3,1,2,3, 4,2,3,4, 5,3,4,5 ),
    ( 5,1,0,1, 2,2,1,2, 3,3,2,3, 4,4,3,4 ),
    ( 4,2,1,0, 1,3,2,1, 2,4,3,2, 3,5,4,3 ),
    ( 3,3,2,1, 0,4,3,2, 1,5,4,3, 2,6,5,4 ),
    ( 5,1,2,3, 4,0,1,2, 3,1,2,3, 4,2,3,4 ),
    ( 4,2,1,2, 3,1,0,1, 2,2,1,2, 3,3,2,3 ),
    ( 3,3,2,1, 2,2,1,0, 1,3,2,1, 2,4,3,2 ),
    ( 2,4,3,2, 1,3,2,1, 0,4,3,2, 1,5,4,3 ),
    ( 4,2,3,4, 5,1,2,3, 4,0,1,2, 3,1,2,3 ),
    ( 3,3,2,3, 4,2,1,2, 3,1,0,1, 2,2,1,2 ),
    ( 2,4,3,2, 3,3,2,1, 2,2,1,0, 1,3,2,1 ),
    ( 1,5,4,3, 2,4,3,2, 1,3,2,1, 0,4,3,2 ),
    ( 3,3,4,5, 6,2,3,4, 5,1,2,3, 4,0,1,2 ),
    ( 2,4,3,4, 5,3,2,3, 4,2,1,2, 3,1,0,1 ),
    ( 1,5,4,3, 4,4,3,2, 3,3,2,1, 2,2,1,0 ),
    ( 0,6,5,4, 3,5,4,3, 2,4,3,2, 1,3,2,1 )
)

def label_at(i, id):
    shift = SHIFT_FOR[i]
    return ((0b1111 << shift) & id) >> shift

SHIFT_FOR = (
    60, 56, 52, 48,
    44, 40, 36, 32,
    28, 24, 20, 16,
    12,  8,  4,  0
)

def adj_id_for(id, i0, next_cell):
    swp = id
    lbl = label_at(next_cell, id)
    sftn = SHIFT_FOR[i0]
    sft0 = SHIFT_FOR[next_cell]
    swp = ((swp & ~(0b1111 << sftn)) | (lbl << sftn)) & ~(0b1111 << sft0)
    return swp

main()