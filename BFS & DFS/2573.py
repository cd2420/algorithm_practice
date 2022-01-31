# 빙산
from collections import deque


def bfs(x, y, visited):
    if visited[x][y] or graph[x][y] != 0:
        return
    visited[x][y] = True
    q = deque([(x, y)])
    tmp_result = []
    while q:
        x, y = q.popleft()
        for dx, dy in directions:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                if graph[nx][ny] == 0:
                    visited[nx][ny] = True
                    q.append((nx, ny))
                else:
                    tmp_result.append((nx, ny))

    return tmp_result


def check_graph():
    visited = [[False] * m for _ in range(n)]
    is_first = True
    for i in range(n):
        for j in range(m):
            if graph[i][j] != 0:
                if is_first:
                    is_first = False
                    check_2(i, j, visited)
                else:
                    if check_2(i, j, visited):
                        return False
    return True


def check_2(x, y, visited):
    if visited[x][y]:
        return False
    visited[x][y] = True
    q = deque([(x, y)])
    while q:
        x, y = q.popleft()
        for dx, dy in directions:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and graph[nx][ny] != 0:
                visited[nx][ny] = True
                q.append((nx, ny))
    return True


directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
year = 0
while True:
    visited = [[False] * m for _ in range(n)]
    check_result = []
    for i in range(n):
        for j in range(m):
            tmp_result = bfs(i, j, visited)
            if tmp_result:
                check_result += tmp_result
    if check_result:
        for x, y in check_result:
            if graph[x][y] > 0:
                graph[x][y] -= 1
        if check_graph():
            year += 1
        else:
            print(year + 1)
            break
    else:
        print(0)
        break
