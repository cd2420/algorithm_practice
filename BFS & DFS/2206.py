# 벽 부수고 이동하기
from collections import deque
directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]


def bfs(x, y):

    checked[x][y][0] = 1
    q = deque([(x, y, 0)])

    while q:
        x, y, status = q.popleft()

        if x == n - 1 and y == m - 1:
            continue
        for dx, dy in directions:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == 0:
                    if checked[nx][ny][status] == 0 or checked[nx][ny][status] > checked[x][y][status] + 1:
                        checked[nx][ny][status] = checked[x][y][status] + 1
                        q.append((nx, ny, status))
                else:
                    if status == 1:
                        continue
                    else:
                        if checked[nx][ny][status + 1] == 0 or checked[nx][ny][status + 1] > checked[x][y][status] + 1:
                            checked[nx][ny][status +
                                            1] = checked[x][y][status] + 1
                            q.append((nx, ny, status + 1))


n, m = map(int, input().split())
graph = [list(map(int, list(input()))) for _ in range(n)]
checked = [[[0, 0] for __ in range(m)] for _ in range(n)]

bfs(0, 0)

r1, r2 = checked[n-1][m-1]
if r1 == r2 == 0:
    print(-1)
else:
    if r1 < r2:
        if r1:
            print(r1)
        else:
            print(r2)
    else:
        if r2:
            print(r2)
        else:
            print(r1)
