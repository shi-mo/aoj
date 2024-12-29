import sys

def test_bags(p:int, w: "List[int]", k: int):
    wbag = 0
    j = 1
    for wi in w:
        if p < wi:
            return False
        wbag += wi
        if p < wbag:
            wbag = wi
            j += 1
    return (j <= k)

def bsearch(pmin: int, pmax: int, w: "List[int]", k: int, test):
    if pmax <= pmin:
        raise Exception('must not happen')
    if 1+pmin == pmax:
        return pmax

    pmid = (pmin+pmax)//2
    if test(pmid, w, k):
        return bsearch(pmin, pmid, w, k, test)
    return bsearch(pmid, pmax, w, k, test)

n,k = [int(w) for w in sys.stdin.readline().split()]
w = []
for _ in range(n):
    w.append(int(sys.stdin.readline()))

print(bsearch(0, sum(w), w, k, test_bags))
