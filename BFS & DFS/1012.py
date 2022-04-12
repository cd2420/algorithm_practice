# 유기농 배추
import sys
from collections import deque

directions = [ (1, 0), (0, 1), (-1, 0), (0, -1)]

def bfs(x, y, graph, m, n):
    if graph[x][y] == 0:
        return False
    q = deque([(x, y)])
    graph[x][y] = 0
    while q:
        x, y = q.popleft()
        for dx, dy in directions:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 1:
                graph[nx][ny] = 0
                q.append((nx, ny))
    return True

input = sys.stdin.readline
for _ in range(int(input())):
    m, n, k = map(int, input().split())
    graph = [[0] * m for __ in range(n)]
    for __ in range(k):
        x, y = map(int, input().split())
        graph[y][x] = 1
    result = 0
    for i in range(n):
        for j in range(m):
            if bfs(i, j, graph, m, n):
                result += 1
    print(result)