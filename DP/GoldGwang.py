# 금광
import sys
input = sys.stdin.readline
for _ in range(int(input())):
    n,m = map(int, input().split())
    dp = [[0] * m for __ in range(n)]
    arr = [[0] * m for __ in range(n)]
    gold = list(map(int, input().split()))
    for i in range(n):
        for j in range(m):
            dp[i][j] = gold[i * m + j]
            arr[i][j] = gold[i * m + j]
    
    for j in range(m-1):
        for i in range(n):
            for dx in [0 , 1, -1]:
                nx = i + dx
                ny = j + 1
                if 0 <= nx < n:
                    dp[nx][ny] = max(dp[nx][ny], dp[i][j] + arr[nx][ny])
    result = -1
    for i in range(n):
        result = max(result, dp[i][-1])
    print(result)