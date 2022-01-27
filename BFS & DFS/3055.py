# 탈출
from collections import deque
directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]


def bfs(x, y, water):

    q = deque([(x, y)])

    while q:

        tmp_water = set()
        for w_x, w_y in water:

            for dx, dy in directions:
                nw_x = w_x + dx
                nw_y = w_y + dy
                if 0 <= nw_x < r and 0 <= nw_y < c and graph[nw_x][nw_y] != 'D' and graph[nw_x][nw_y] != 'X' and graph[nw_x][nw_y] != '*':
                    graph[nw_x][nw_y] = '*'
                    tmp_water.add((nw_x, nw_y))
        water = tmp_water
        tmp_q = []
        while q:
            x, y = q.popleft()
            if graph[x][y] == 'D':
                return checked[x][y]

            for dx, dy in directions:
                nx = x + dx
                ny = y + dy
                if 0 <= nx < r and 0 <= ny < c and (graph[nx][ny] == '.' or graph[nx][ny] == 'D'):
                    if checked[nx][ny] == 0 or checked[nx][ny] > checked[x][y] + 1:
                        checked[nx][ny] = checked[x][y] + 1
                        tmp_q.append((nx, ny))
        q = deque(tmp_q)

    return 'KAKTUS'


r, c = map(int, input().split())
graph = [list(input()) for _ in range(r)]
checked = [[0] * c for _ in range(r)]
tmp_q = []
water = set()
for x in range(len(graph)):
    for y in range(len(graph[x])):
        if graph[x][y] == 'S':
            tmp_q = [x, y]
        if graph[x][y] == '*':
            water.add((x, y))

start_x, start_y = tmp_q

print(bfs(start_x, start_y, water))
