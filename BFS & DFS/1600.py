# 말이 되고픈 원숭이
from collections import deque

directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
horse = [(2, 1), (2, -1), (1, 2), (1, -2),
         (-2, 1), (-2, -1), (-1, 2), (-1, -2)]


def bfs(x, y):
    q = deque([(x, y, 0)])
    while q:
        x, y, h_cnt = q.popleft()

        if x == h - 1 and y == w - 1:
            continue
        # 원숭이로 가는 법
        for dx, dy in directions:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < h and 0 <= ny < w and graph[nx][ny] == 0:
                if count[nx][ny][h_cnt] == 0 or count[nx][ny][h_cnt] > count[x][y][h_cnt] + 1:
                    count[nx][ny][h_cnt] = count[x][y][h_cnt] + 1
                    q.append((nx, ny, h_cnt))

        # 말로 가는 법
        if h_cnt < k:
            for hx, hy in horse:
                hx = x + hx
                hy = y + hy
                if 0 <= hx < h and 0 <= hy < w and graph[hx][hy] == 0:
                    if count[hx][hy][h_cnt + 1] == 0 or count[hx][hy][h_cnt + 1] > count[x][y][h_cnt] + 1:
                        count[hx][hy][h_cnt + 1] = count[x][y][h_cnt] + 1
                        q.append((hx, hy, h_cnt + 1))


k = int(input())
w, h = map(int, input().split())
if w == 1 and h == 1:
    print(0)
else:
    graph = [list(map(int, input().split())) for _ in range(h)]
    count = [[[0] * (k + 1) for __ in range(w)] for _ in range(h)]

    bfs(0, 0)

    result = list(set(count[h-1][w-1]))
    result.sort()
    if len(result) == 1 and result[0] == 0:
        print(-1)
    else:
        if result[0] != 0:
            print(result[0])
        else:
            print(result[1])
