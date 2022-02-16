# 인구 이동
from collections import deque

directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]


def bfs(x, y):
    if visited[x][y]:
        return False
    visited[x][y] = True
    q = deque([(x, y)])
    return_data = set()
    return_data.add((x, y))
    while q:
        x, y = q.popleft()
        for dx, dy in directions:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                if L <= abs(graph[x][y] - graph[nx][ny]) <= R:
                    return_data.add((nx, ny))
                    visited[nx][ny] = True
                    q.append((nx, ny))
    return return_data


n, L, R = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
count = 0
while True:
    visited = [[False] * n for _ in range(n)]
    is_break = True
    for i in range(n):
        for j in range(n):
            tmp_result = bfs(i, j)
            if tmp_result and len(tmp_result) > 1:
                is_break = False
                change_data = sum(graph[x][y]
                                  for x, y in tmp_result) // len(tmp_result)
                for tmp_x, tmp_y in tmp_result:
                    graph[tmp_x][tmp_y] = change_data
    if is_break:
        break
    else:
        count += 1
print(count)
