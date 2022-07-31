# 프로그래머스
# 아이템줍기
from collections import deque

directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = 1e9
    graph = [[2] * 104 for _ in range(104)]
    visited = [[False] * 104 for _ in range(104)]
    characterX *= 2
    characterY *= 2
    itemX *= 2
    itemY *= 2
    for x1, y1, x2, y2 in rectangle:
        t_x1 = x1 * 2
        t_x2 = x2 * 2
        t_y1 = y1 * 2
        t_y2 = y2 * 2
        for x in range(t_x1, t_x2+1):
            if graph[x][t_y1] == 2:
                graph[x][t_y1] = 0
            if graph[x][t_y2] == 2:
                graph[x][t_y2] = 0
        for y in range(t_y1, t_y2+1):
            if graph[t_x1][y] == 2:
                graph[t_x1][y] = 0
            if graph[t_x2][y] == 2:
                graph[t_x2][y] = 0
        for x in range(t_x1+1, t_x2):
            for y in range(t_y1+1, t_y2):
                graph[x][y] = 1
    
    q = deque([(characterX, characterY, 0)])
    visited[characterX][characterY] = True
    while q:
        x, y, cnt = q.popleft()
        if x == itemX and y == itemY:
            answer = min(answer, cnt)
            continue
        for dx, dy in directions:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < 104 and 0 <= ny < 104 and not visited[nx][ny]:
                if graph[nx][ny] == 0:
                    visited[nx][ny] = True
                    q.append((nx, ny, cnt + 1))

    return answer // 2