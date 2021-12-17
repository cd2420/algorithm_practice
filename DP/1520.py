# 내리막 길
import sys
directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
sys.setrecursionlimit(10**6)


def dfs(x, y):

    if x == n-1 and y == m-1:
        return 1
    if dp[x][y] != -1:
        return dp[x][y]
    dp[x][y] = 0
    cnt = 0
    for dx, dy in directions:
        nx = x + dx
        ny = y + dy
        if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] < graph[x][y]:
            dp[x][y] += dfs(nx, ny)
            cnt = dp[x][y]
    return cnt


n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
dp = [[-1] * m for _ in range(n)]
dfs(0, 0)
print(dp[0][0])
