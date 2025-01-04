def main():
    matches = kmp_2d_search(*load_input())
    for i, j in matches:
        print(f'{i} {j}')

def load_input():
    h, w, mat  = load_mat()
    r, c, part = load_mat()
    return (h, w, mat, r, c, part)

def load_mat():
    h, w = [int(x) for x in input().split()]
    mat = []
    for i in range(h):
        mat.append(input())
    return (h, w, mat)

def kmp_2d_search(h, w, mat, r, c, part):
    lps = build_kmp2d_table(r, c, part)
    matches = []
    for i in range(h-r+1):
        j = 0
        while j < (w-c+1):
            match = True
            for k in range(r):
                if mat[i+k][j:j+c] != part[k]:
                    match = False
                    break
            if match:
                matches.append((i, j))
                j += 1
                continue
            if 0 == k:
                j += 1
                continue
            j += c - lps[k-1][-1] # Use LPS to shift
    return matches

def build_kmp2d_table(r, c, pattern):
    return [build_kmp_table(c, pattern[i]) for i in range(r)]

def build_kmp_table(n, p):
    table = [0] * n
    len = 0
    for j in range(1, n):
        while 0 < len and p[j] != p[len]:
            len = table[len-1]
        if p[j] == p[len]:
            len += 1
        table[j] = len
    return table

main()