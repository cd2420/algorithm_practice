# 동전 2
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]
coins.insert(0, 0)
coins.sort()
dp = [[1e9] * (k+1) for _ in range(n + 1)]
for i in range(1, n+1):
    for j in range(1, k+1):
        if coins[i] > j:
            dp[i][j] = dp[i-1][j]
        elif j == coins[i]:
            dp[i][j] = min(1, dp[i-1][j])
        else:
            dp[i][j] = min(dp[i][j - coins[i]] + 1, dp[i-1][j])

if dp[-1][-1] == 1e9:
    print(-1)
else:
    print(dp[-1][-1])
