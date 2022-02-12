# 동전 바꿔주기
t = int(input())
k = int(input())
coin = [[0, 0]]
for _ in range(k):
    a, b = map(int, input().split())
    coin.append([a, b])
dp = [[0] * (t + 1) for _ in range(k + 1)]
dp[0][0] = 1
for i in range(1, k+1):
    val, cnt = coin[i]
    for j in range(t + 1):
        dp[i][j] = dp[i-1][j]
        for v in range(1, cnt + 1):
            if j - v * val >= 0:
                dp[i][j] += dp[i-1][j - v*val]
            else:
                break
print(dp[k][t])
