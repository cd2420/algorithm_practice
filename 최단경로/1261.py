# 알고스팟
import heapq
import sys

input = sys.stdin.readline
directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]


def dkstra(x, y):
    q = []
    bricked[x][y] = 0
    heapq.heappush(q, (0, x, y))

    while q:
        bricks, x, y = heapq.heappop(q)

        if x == n - 1 and y == m - 1:
            continue

        for dx, dy in directions:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < n and 0 <= ny < m:
                if bricked[nx][ny] == 1e9:
                    tmp_bricks = bricks
                    if graph[nx][ny] == 1:
                        tmp_bricks += 1
                    bricked[nx][ny] = tmp_bricks
                    heapq.heappush(q, (tmp_bricks, nx, ny))


m, n = map(int, input().split())
graph = [list(map(int, list(input().rstrip()))) for _ in range(n)]
bricked = [[1e9] * m for _ in range(n)]

dkstra(0, 0)
print(bricked[-1][-1])
