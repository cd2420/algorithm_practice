# 청소년 상어
from copy import deepcopy


directions = [(-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1)]

def dfs(graph, shark_x, shark_y, cnt):
    global answer
    graph = deepcopy(graph)
    
    cnt += graph[shark_x][shark_y][0]
    graph[shark_x][shark_y][0] = -1

    move_all_fish(graph, shark_x, shark_y)

    nxt_cand = find_nxt_fish(graph, shark_x, shark_y)
    if not nxt_cand:
        answer = max(answer, cnt)
        return
    for nxt_x, nxt_y in nxt_cand:
        dfs(graph, nxt_x, nxt_y, cnt)

def move_all_fish(graph, shark_x, shark_y):
    for i in range(1, 17):
        fish = find_fish(graph, i)
        if fish:
            x, y = fish
            dir = graph[x][y][1]
            for j in range(8):
                dx, dy = directions[dir]
                nx = x + dx
                ny = y + dy
                if 0 <= nx < 4 and 0 <= ny < 4:
                    if shark_x != nx or shark_y != ny:
                        graph[x][y][1] = dir
                        graph[x][y], graph[nx][ny] = graph[nx][ny], graph[x][y]
                        break
                dir = turn_left(dir)

def find_fish(graph, x):
    for i in range(4):
        for j in range(4):
            if graph[i][j][0] == x:
                return (i, j)
    return None

def turn_left(dir):
    return (dir + 1) % 8

def find_nxt_fish(graph, shark_x, shark_y):
    result = []
    dx, dy = directions[graph[shark_x][shark_y][1]]
    shark_x += dx
    shark_y += dy
    while 0 <= shark_x < 4 and 0 <= shark_y < 4:
        if graph[shark_x][shark_y][0] != -1:
            result.append((shark_x, shark_y))
        shark_x += dx
        shark_y += dy
    return result

graph = [[None] * 4 for _ in range(4)]
for i in range(4):
    tmp_lst = list(map(int, input().split()))
    for j in range(4):
        graph[i][j] = [tmp_lst[2 * j], tmp_lst[2 * j + 1] - 1]
answer = 0
dfs(graph, 0, 0, 0)
print(answer)