def gen_dp(n):
    dp = [[None]*n for _ in range(n)]
    for i in range(n):
        dp[i][i] = 0
    return dp

def solve_mcmp(n, rc, dp, i, j):
    if dp[i][j] is not None:
        return dp[i][j]
    if j <= i+1:
        dp[i][j] = rc[i][0] * rc[j][0] * rc[j][1]
        return dp[i][j]

    for k in range(i,j):
        l = solve_mcmp(n,rc,dp,i,k)
        r = solve_mcmp(n,rc,dp,k+1,j)
        m = l + r + (rc[i][0] * rc[k][1] * rc[j][1])
        if dp[i][j] is None or m < dp[i][j]:
            dp[i][j] = m
    return dp[i][j]

n = int(input())
rc = []
for _ in range(n):
    r,c = [int(x) for x in input().split()]
    rc.append([r,c])

dp = gen_dp(n)
print(solve_mcmp(n,rc,dp,0,n-1))
