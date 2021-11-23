# 삼각그래프
import sys
input = sys.stdin.readline

direction_by_col = {
    0: [(1, 0), (0, 1), (1, 1)],
    1: [(1, 0), (0, 1), (1, 1), (1, -1)],
    2: [(1, -1), (1, 0)]
}

tc = 1
while True:
    n = int(input())
    if n == 0:
        break
    graph = [list(map(int, input().split())) for _ in range(n)]
    dp = [[1e9] * 3 for _ in range(n)]

    dp[0][1] = graph[0][1]
    for j in range(1, 3):
        for dx, dy in direction_by_col[j]:
            nx = dx
            ny = j + dy
            if 0 <= nx < n and 0 <= ny < 3 and dp[nx][ny] > dp[0][j] + graph[nx][ny]:
                dp[nx][ny] = dp[0][j] + graph[nx][ny]

    for i in range(1, n):
        for j in range(3):
            for dx, dy in direction_by_col[j]:
                nx = i + dx
                ny = j + dy
                if 0 <= nx < n and 0 <= ny < 3 and dp[nx][ny] > dp[i][j] + graph[nx][ny]:
                    dp[nx][ny] = dp[i][j] + graph[nx][ny]

    print(str(tc) + ". " + str(dp[-1][1]))
    tc += 1
