# 알약
dp = [[0] * 31 for _ in range(31)]
# i 는 W개수, j는 H개수
for i in range(1, 31):
    dp[i][1] = i
    for j in range(2, i+1):
        dp[i][j] = dp[i][j-1] + dp[i-1][j]

for _ in range(1000):
    n = int(input())
    if n == 0:
        break
    print(dp[n][n])
