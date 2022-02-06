# 1,2,3 더하기 4
import sys
input = sys.stdin.readline

for _ in range(int(input().rstrip())):
    n = int(input().rstrip())
    dp = [[0, 0, 0] for _ in range(n + 1)]
    dp[1][0] = 1
    if n > 1:
        dp[2][0] = 1
        dp[2][1] = 1
    if n > 2:
        dp[3][0] = 2
        dp[3][2] = 1
    for i in range(4, n+1):
        dp[i][0] = sum(dp[i-1])
        dp[i][1] = dp[i-2][1] + dp[i-2][2]
        dp[i][2] = dp[i-3][2]
    print(sum(dp[-1]))
