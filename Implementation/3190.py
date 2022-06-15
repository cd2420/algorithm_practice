# 뱀
from collections import deque
directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

n = int(input())
k = int(input())
apples = [[0] * (n+1) for _ in range(n+1)]
for _ in range(k):
    a, b = map(int, input().split())
    apples[a][b] = 1

l = int(input())
turnIdx = {}
for _ in range(l):
    a, b = input().split()
    turnIdx[int(a)] = b

snake = deque([(1, 1)])
result = 0
dir = 0
while True:
    if result in turnIdx:
        if turnIdx[result] == 'D':
            dir = (dir + 1) % 4
        else :
            dir = (dir + 3) % 4
    dx, dy = directions[dir]
    nx = snake[-1][0] + dx
    ny = snake[-1][1] + dy
    if 0 < nx <= n and 0 < ny <= n and (nx, ny) not in snake:
        result += 1
        snake.append((nx, ny))
        if not apples[nx][ny]:
            snake.popleft()
        else :
            apples[nx][ny] = 0
    else :
        break

print(result + 1)
