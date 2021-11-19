# 카드 구매하기 2
import sys
input = sys.stdin.readline
n = int(input())
cards = list(map(int, input().split()))
cards.insert(0, 0)
dp = [[1e9] * (n + 1) for _ in range(n+1)]

for i in range(1, n+1):
    dp[1][i] = cards[1] * i

for i in range(2, n+1):
    for j in range(1, n+1):
        if i > j:
            dp[i][j] = dp[i-1][j]
        elif i == j:
            dp[i][j] = min(dp[i-1][j], cards[i])
        else:
            dp[i][j] = min(dp[i-1][j], cards[i] + dp[i][j-i])
print(dp[-1][-1])
