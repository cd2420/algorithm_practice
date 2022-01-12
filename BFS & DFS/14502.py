# 연구소
from collections import deque
import copy


def check(x, y, cnt):
    global result
    if cnt == 3:
        tmp_graph = copy.deepcopy(graph)
        for i in range(n):
            for j in range(m):
                bfs(i, j, tmp_graph)

        result = max(result, check_0(tmp_graph))
        return
        # result = max(bfs(graph[:]), result)

    for i in range(x, n):
        for j in range(y, m):
            if graph[i][j] == 0:
                graph[i][j] = 1
                check(i, j, cnt + 1)
                graph[i][j] = 0
        y = 0


def bfs(x, y, tmp_graph):
    if tmp_graph[x][y] != 2:
        return

    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    q = deque([(x, y)])
    while q:
        x, y = q.popleft()
        for dx, dy in directions:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < n and 0 <= ny < m and tmp_graph[nx][ny] == 0:
                tmp_graph[nx][ny] = 2
                q.append((nx, ny))
    return check_0(tmp_graph)


def check_0(tmp_graph):
    count_0 = 0
    for tmp in tmp_graph:
        for no_virus in tmp:
            if no_virus == 0:
                count_0 += 1
    return count_0


n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]
result = -1
check(0, 0, 0)
print(result)
