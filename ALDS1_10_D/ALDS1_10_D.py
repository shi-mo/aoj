n = int(input())
p = [float(x) for x in input().split()]
q = [float(x) for x in input().split()]

dp = [[None]*n for _ in range(n)]
sb = [[None]*n for _ in range(n)]

for w in range(n):
    for i in range(n-w):
        if w <= 0:
            dp[i][i] = p[i] + (2*(q[i]+q[i+1]))
            sb[i][i] = p[i] + q[i] + q[i+1]
            continue

        j = i+w
        sum = sb[i][j-1] + p[j] + q[j+1]
        sb[i][j] = sum

        t = q[i] + dp[i+1][j]
        for k in range(i+1,j):
            s = dp[i][k-1] + dp[k+1][j]
            if s < t: t = s
        s = dp[i][j-1] + q[j+1]
        if s < t: t = s
        dp[i][j] = sum + t

print(f'{dp[0][n-1]:.8f}')
