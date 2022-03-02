# 레이저 통신
from collections import deque


def bfs(x, y, dir):
    q = deque([(x, y, dir)])

    while q:
        x, y, dir = q.popleft()
        if x == end[0] and y == end[1]:
            continue
        for ndir in range(4):
            dx, dy = directions[ndir]
            nx = x + dx
            ny = y + dy
            if 0 <= nx < h and 0 <= ny < w and graph[nx][ny] != '*' and not (nx == start[0] and ny == start[1]):

                if dir % 2 != ndir % 2:
                    if mirror[nx][ny][ndir] > mirror[x][y][dir] + 1:
                        mirror[nx][ny][ndir] = mirror[x][y][dir] + 1
                        q.append((nx, ny, ndir))
                else:
                    if mirror[nx][ny][ndir] > mirror[x][y][dir]:
                        mirror[nx][ny][ndir] = mirror[x][y][dir]
                        q.append((nx, ny, ndir))


directions = [[-1, 0], [0, 1], [1, 0], [0, -1]]
w, h = map(int, input().split())
graph = [list(input()) for _ in range(h)]
tmp = []
for i in range(h):
    for j in range(w):
        if graph[i][j] == 'C':
            tmp.append((i, j))
start = tmp[0]
end = tmp[1]

mirror = [[[1e9, 1e9, 1e9, 1e9] for _ in range(w)] for __ in range(h)]

for i in range(4):
    dx, dy = directions[i]
    nx = start[0] + dx
    ny = start[1] + dy
    if 0 <= nx < h and 0 <= ny < w and graph[nx][ny] != '*':
        mirror[nx][ny][i] = 0
        bfs(nx, ny, i)
result = mirror[end[0]][end[1]]
result = list(set(result))
if len(result) == 1:
    if result[0] == 1e9:
        print(0)
    else:
        print(result[0])
else:
    print(min(result))
