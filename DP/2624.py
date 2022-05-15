# 동전 바꿔주기
t = int(input())
k = int(input())
coins = [list(map(int, input().split())) for _ in range(k)]
dp = [[0] * (t+1) for _ in range(k+1)]
dp[0][0] = 1
for i in range(1, k+1):
    coin, val = coins[i-1]
    for j in range(t+1):
        dp[i][j] = dp[i-1][j]
        for cnt in range(1, val+1):
            check = coin * cnt
            if check > j:
                break
            dp[i][j] += dp[i-1][j-check]

print(dp[-1][-1])