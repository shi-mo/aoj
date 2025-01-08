from heapq import heapify, heappush, heappop

def main():
    s = input()
    freq_of = count_freq_in(s)
    heap = make_heap_from(freq_of)
    tree = build_tree_from(heap)
    code_len_of = count_code_len_from(tree)
    print(count_len_of(s, code_len_of))

def count_freq_in(s):
    freq_of = {}
    for c in s:
        if c not in freq_of:
            freq_of[c] = 1
            continue
        freq_of[c] += 1
    return freq_of

def make_heap_from(freq_of):
    heap = [(freq, c, True, None) for c, freq in freq_of.items()]
    heapify(heap)
    return heap

def build_tree_from(heap):
    while 2 <= len(heap):
        node1 = heappop(heap)
        fr1, c1, _, _ = node1
        node2 = heappop(heap)
        fr2, c2, _, _ = node2
        heappush(heap, ((fr1 + fr2), (c2+c1), False, (node2, node1)))
    return heap

def count_code_len_from(tree):
    root = tree[0]
    fr, c, leaf, _ = root
    if leaf: return { c: 1 }
    return dict(count_code_len(root, 0))

def count_code_len(node, len):
    _, c, leaf, tree = node
    if leaf: return [(c, len)]
    left, right = tree
    return count_code_len(left, len+1) \
           + count_code_len(right, len+1)

def count_len_of(s, code_len_of):
    cnt = 0
    for c in s:
        cnt += code_len_of[c]
    return cnt

main()