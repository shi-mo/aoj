def main():
    n, wmax, vw = load_input()
    items = order_items(n, vw)
    sumv = 0; sumw = 0
    for vpw, vi, wi in items:
        space = wmax - sumw
        if space <= 0: break
        if wi <= space:
            sumw += wi
            sumv += vi
            continue
        sumw = wmax
        sumv += vpw * space
        break
    fmt = '%d' if 0 == sumv%1 else '%.8f'
    print(fmt % sumv)

def load_input():
    n, w = [int(x) for x in input().split()]
    vw = []
    for i in range(n):
        vw.append([int(x) for x in input().split()])
    return n, w, vw

def order_items(n, vw):
    items = []
    for vi, wi in vw:
        vpw = float(vi) / wi
        items.append((vpw, vi, wi))
    items.sort(reverse=True)
    return items

main()