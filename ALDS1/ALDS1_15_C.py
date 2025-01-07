from bisect import bisect_left, insort_left

def main():
    print(solve(load_input()))

def load_input():
    n = int(input())
    acts = []
    for _ in range(n):
        si, ti = [int(x) for x in input().split()]
        acts.append((si, ti))
    return acts

def solve(acts):
    acts.sort(key=lambda a: a[1])
    ans = 0
    last_t = 0
    for s, t in acts:
        if s <= last_t: continue
        last_t = t
        ans += 1
    return ans

main()