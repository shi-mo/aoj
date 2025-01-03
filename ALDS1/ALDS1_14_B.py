def main():
    t = input()
    p = input()

    for pos in find_all_matches_in(t, p):
        print(pos)

def find_all_matches_in(t, p):
    lt, lp = len(t), len(p)
    if 0 == lp: return []

    matches = []
    kmp_tbl = build_kmp_table(p)
    cursor_p = 0
    for i in range(lt):
        while 0 < cursor_p and t[i] != p[cursor_p]:
            cursor_p = kmp_tbl[cursor_p - 1]
        if t[i] == p[cursor_p]:
            cursor_p += 1
        if cursor_p == lp:
            matches.append(i - lp + 1)
            cursor_p = kmp_tbl[cursor_p - 1]
    return matches

def build_kmp_table(p):
    n = len(p)
    table = [0] * n
    j = 0
    for i in range(1, n):
        while 0 < j and p[i] != p[j]:
            j = table[j - 1]
        if p[i] == p[j]:
            j += 1
        table[i] = j
    return table

main()