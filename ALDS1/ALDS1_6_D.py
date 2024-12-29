n = int(input())
w = [int(x) for x in input().split()]
ws = sorted(w)

cost = 0
for cyc_min in range(n):
    idx = w.index(ws[cyc_min])
    cyc_len = 0
    while cyc_min < idx:
        cyc_len += 1
        idx_pre = w.index(ws[idx])
        cost += ws[idx]
        w[idx],w[idx_pre] = w[idx_pre],w[idx]
        idx = idx_pre
    cost_in_cyc = ws[cyc_min] * cyc_len
    cost_borrow = ws[cyc_min]*2 + ws[0]*(cyc_len+2)
    cost += min(cost_in_cyc, cost_borrow)
print(cost)
