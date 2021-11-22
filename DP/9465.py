# 스티커
import sys
input = sys.stdin.readline
for _ in range(int(input())):
    n = int(input())
    stickers = [list(map(int, input().split())) for __ in range(2)]
    dp = [[0, 0] for __ in range(n)]
    dp[0][0] = stickers[0][0]
    dp[0][1] = stickers[1][0]
    for i in range(1, n):
        dp[i][0] = max(dp[i-1][1] + stickers[0][i], dp[i-1][0])
        dp[i][1] = max(dp[i-1][0] + stickers[1][i], dp[i-1][1])
    print(max(dp[-1]))
