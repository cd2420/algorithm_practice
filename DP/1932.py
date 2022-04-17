# 정수 삼각형
n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
dp = [[-1] * i for i in range(1, n+1)]
dp[0][0] = graph[0][0]
for i in range(n-1):
    row = graph[i]
    for j in range(len(row)):
        dp[i+1][j] = max(dp[i+1][j], dp[i][j] + graph[i+1][j])
        dp[i+1][j+1] = max(dp[i+1][j+1], dp[i][j] + graph[i+1][j+1])

print(max(dp[-1]))


