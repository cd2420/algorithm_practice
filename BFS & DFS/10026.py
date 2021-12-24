# 적록색약
from collections import deque

directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
check = {
    'R': 0, 'G': 1, 'B': 4
}


def bfs(x, y, visited, type):

    if visited[x][y]:
        return False
    else:
        visited[x][y] = True

    rgb = check[graph[x][y]]
    q = deque([(x, y)])
    while q:
        x, y = q.popleft()
        for dx, dy in directions:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < n and 0 <= ny < n:
                if type == 0 and rgb == check[graph[nx][ny]] and not visited[nx][ny]:
                    visited[nx][ny] = True
                    q.append((nx, ny))
                if type == 1 and abs(rgb - check[graph[nx][ny]]) <= 1 and not visited[nx][ny]:
                    visited[nx][ny] = True
                    q.append((nx, ny))
    return True


n = int(input())
graph = [input() for _ in range(n)]

# 일반인
result1 = 0
visited1 = [[False] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if bfs(i, j, visited1, 0):
            result1 += 1

# 적록
result2 = 0
visited2 = [[False] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if bfs(i, j, visited2, 1):
            result2 += 1

print(result1, result2)
