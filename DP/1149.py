# RGB거리
import sys
input = sys.stdin.readline
n = int(input())
house = [list(map(int, input().split())) for _ in range(n)]
dp = house[:]
for i in range(1, n):
    dp[i][0] = min(dp[i-1][1] + house[i][0], dp[i-1][2] + house[i][0])
    dp[i][1] = min(dp[i-1][0] + house[i][1], dp[i-1][2] + house[i][1])
    dp[i][2] = min(dp[i-1][0] + house[i][2], dp[i-1][1] + house[i][2])
print(min(dp[-1]))
