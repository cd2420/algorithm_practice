# 최대 정사각형
import sys
input = sys.stdin.readline

while True:
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break
    dp = [list(map(int, input().split())) for _ in range(n)]
    result = 0
    for i in range(1, n):
        for j in range(1, m):
            if dp[i][j] != 0:
                dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1

    for d in dp:
        result = max(result, max(d))
    print(result)
