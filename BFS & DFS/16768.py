# Mooyo Mooyo
from collections import deque
directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

def bfs():
    result = 0
    for x in range(N):
        for y in range(10):
            if graph[x][y] == '0':
                continue
            check = set()
            q = deque([(x, y, graph[x][y])])
            check.add((x, y))
            while q:
                _x, _y, num = q.popleft()
                for dx, dy in directions:
                    nx = _x + dx
                    ny = _y + dy
                    if 0 <= nx < N and 0 <= ny < 10 and graph[nx][ny] == num and (nx, ny) not in check:
                        check.add((nx, ny))
                        q.append((nx, ny, num))
            if len(check) >= K:
                result += len(check)
                for cx, cy in check:
                    graph[cx][cy] = '0'

    return result

def move():
    for j in range(10):
        check = 0
        for i in range(N-1, -1, -1):
            if graph[i][j] == '0':
                check += 1
                continue
            graph[i+check][j], graph[i][j] = graph[i][j], graph[i+check][j]
            

N, K = map(int, input().split())
graph = [list(input()) for _ in range(N)]

while True:
    if bfs():
        move()
    else :
        break
for g in graph:
    print(''.join(g))