# 동전
import sys
input = sys.stdin.readline
for _ in range(int(input())):
    n = int(input())
    coins = list(map(int, input().split()))
    m = int(input())
    dp = [[0] * 10001 for _ in range(21)]
    for i in range(1, n+1):
        dp[i][coins[i-1]] = 1

    for money in range(1, m+1):
        for c in range(1, n+1):
            coin = coins[c-1]
            if coin > money:
                dp[c][money] = dp[c-1][money]
            else:
                dp[c][money] = dp[c-1][money] + \
                    dp[c][money] + dp[c][money - coin]
    print(dp[n][m])
