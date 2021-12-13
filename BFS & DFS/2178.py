# 미로 탐색
from collections import deque
n, m = map(int, input().split())
graph = []
for _ in range(n):
    tmp_row = []
    for i in input():
        tmp_row.append(int(i))
    graph.append(tmp_row)
direction = [(1, 0), (0, 1), (-1, 0), (0, -1)]
q = deque([(0, 0)])
while q:
    x, y = q.popleft()
    if x == n and y == m:
        continue
    for dx, dy in direction:
        nx = x + dx
        ny = y + dy
        if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 1:
            graph[nx][ny] += graph[x][y]
            q.append((nx, ny))
print(graph[-1][-1])
