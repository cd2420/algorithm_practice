# 점프
def dfs(start):
    x, y = start
    if graph[x][y] == 0:
        if x == N - 1 and y == N - 1:
            return 1
        else:
            return 0
    if dp[x][y] != -1:
        return dp[x][y]
    dp[x][y] = 0
    count = 0
    for dx, dy in [(graph[x][y], 0), (0, graph[x][y])]:
        nx = x + dx
        ny = y + dy
        if 0 <= nx < N and 0 <= ny < N:
            count += dfs((nx, ny))
    dp[x][y] = count
    return count


N = int(input())
graph = [[] for _ in range(N)]
for i in range(N):
    graph[i] = list(map(int, input().split()))
dp = [[-1] * N for _ in range(N)]
dfs((0, 0))
print(dp[0][0])
