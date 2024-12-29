import sys

def solve(dp, a, n, i, m):
    if 0 == m: return True
    if m <  0: return False
    if n <= i: return False
    if dp[i][m] is None:
        dp[i][m] = solve(dp,a,n,i+1,m-a[i]) or solve(dp,a,n,i+1,m)
    return dp[i][m]

n = int(sys.stdin.readline())
a = [int(w) for w in sys.stdin.readline().split()]
q = int(sys.stdin.readline())
m = [int(w) for w in sys.stdin.readline().split()]

mmax = max(m)
dp = [[None]*(mmax+1) for _ in range(n)]

for mi in m:
    print('yes' if solve(dp,a,n,0,mi) else 'no')
