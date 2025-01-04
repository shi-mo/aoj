def main():
    init()
    mat,  h, w = load_matrix()
    part, r, c = load_matrix()

    rhm = rolling_hash(mat, h, w)
    rhp = rolling_hash(part, r, c)
    hash = rhp[-1][-1]
    for i in range(h-r+1):
        for j in range(w-c+1):
            if hash == part_hash_at(rhm, j, i, j+c, i+r):
                print(f'{i} {j}')

MOD = 10**9 + 9
P = 13; Q = 19
P_POW = Q_POW = None

def init():
    len = 1001
    global P_POW, Q_POW
    P_POW = [1] * (len+1)
    Q_POW = [1] * (len+1)
    for i in range(len):
        P_POW[i+1] = P_POW[i] * P % MOD
        Q_POW[i+1] = Q_POW[i] * Q % MOD

def load_matrix():
    h, w = [int(x) for x in input().split()]
    mat = []
    for i in range(h):
        mat.append(input())
    return mat, h, w

def rolling_hash(mat, h, w):
    rh = [[0]*(w+1) for i in range(h+1)]
    for i in range(h):
        sum = 0
        rhi = rh[i]
        rhn = rh[i+1]
        mi  = mat[i]
        for j in range(w):
            v = ord(mi[j])
            sum = (sum * P + v) % MOD
            rhn[j+1] = (sum + (rhi[j+1] * Q)) % MOD
    return rh

def part_hash_at(rh, x0, y0, x1, y1):
    p = P_POW[x1 - x0]
    q = Q_POW[y1 - y0]
    hash  = rh[y1][x1]
    hash -= (rh[y1][x0] * p) + (rh[y0][x1] * q)
    hash += rh[y0][x0] * (p * q) % MOD
    return hash % MOD

main()