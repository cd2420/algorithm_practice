# 게임 맵 최단거리
from collections import deque


def bfs(maps):
    start = (0, 0)
    que = deque([start])
    while que:
        x, y = que.popleft()

        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nx = x + dx
            ny = y + dy
            if nx < 0 or ny < 0 or nx >= len(maps) or ny >= len(maps[0]) or (nx == 0 and ny == 0):
                continue
            if maps[nx][ny] != 1:
                continue

            maps[nx][ny] = maps[x][y] + 1
            que.append((nx, ny))


def solution(maps):
    n = len(maps)
    m = len(maps[0])
    bfs(maps)
    if maps[n-1][m-1] != 1:
        return maps[n-1][m-1]
    else:
        return -1
