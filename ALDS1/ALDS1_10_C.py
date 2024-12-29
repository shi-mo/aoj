def lcs_for(x: str, y: str):
    n,m = len(x),len(y)
    dp = [0]*(m+1)

    for a in x:
        dp_pre = dp.copy()
        for j,b in enumerate(y):
            if a == b:
                dp[j+1] = dp_pre[j] + 1
            elif dp[j+1] < dp[j]:
                dp[j+1] = dp[j]
    return dp[m]

n = int(input())
for _ in range(n):
    x = input()
    y = input()
    print(lcs_for(x,y))
