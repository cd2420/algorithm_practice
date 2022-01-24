# 아기 상어
from collections import deque

directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]


def check_level_up():

    check = len(level)
    for l in level:
        if l:
            check -= 1

    if check:
        return False
    else:
        return True


def bfs(start_x, start_y):
    visited = [[0] * n for _ in range(n)]
    q = deque([(start_x, start_y)])

    check = []
    while q:
        x, y = q.popleft()

        if can_eat(graph[x][y]):
            check.append((x, y, visited[x][y]))
            continue

        for dx, dy in directions:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] != 9 and if_pass(graph[nx][ny]):
                if not visited[nx][ny] or visited[nx][ny] > visited[x][y] + 1:
                    visited[nx][ny] = visited[x][y] + 1
                    q.append((nx, ny))
    if check:
        check.sort(key=lambda x: (x[2], x[0], x[1]))
    return check


def can_eat(num):
    if len(level) <= num or num == 0 or num == 9:
        return False
    else:
        return True


def if_pass(num):
    if not num:
        return True
    elif len(level) >= num:
        return True
    else:
        return False


def act_eat(level):
    for l in level:
        if not l:
            l.append(True)
            break


n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

start_x, start_y = 0, 0
for i in range(len(graph)):
    is_break = False
    for j in range(len(graph[i])):
        if graph[i][j] == 9:
            start_x, start_y = i, j
            is_break = True
            break
    if is_break:
        break

level = [[], []]
result = 0
while True:
    # result += bfs(start_x, start_y)
    if result == 43:
        result
    tmp_result = bfs(start_x, start_y)
    if tmp_result:
        nx, ny, time = tmp_result[0]

        act_eat(level)
        if check_level_up():
            level = [[] for _ in range(len(level) + 1)]

        graph[start_x][start_y] = 0
        graph[nx][ny] = 9
        start_x, start_y = nx, ny
        result += time
    else:
        break
print(result)
