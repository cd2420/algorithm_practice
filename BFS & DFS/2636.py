# 치즈
from collections import deque

directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]


def bfs(x, y):
    q = deque([(x, y)])
    visited = [[False] * c for _ in range(r)]
    visited[x][y] = True
    check = set()

    while q:
        x, y = q.popleft()
        for dx, dy in directions:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < r and 0 <= ny < c and not visited[nx][ny]:
                if cheeze[nx][ny] == 0:
                    visited[nx][ny] = True
                    q.append((nx, ny))
                else:
                    if cheeze[x][y] == 0:
                        check.add((nx, ny))
    if check:
        for _check in check:
            x, y = _check
            cheeze[x][y] = 0
    return len(check)


r, c = map(int, input().split())

cheeze = [list(map(int, input().split())) for _ in range(r)]

result = 0
count = 0
while True:
    tmp_count = bfs(0, 0)
    if tmp_count:
        count = tmp_count
        result += 1
        continue
    else:
        break
print(result)
print(count)
