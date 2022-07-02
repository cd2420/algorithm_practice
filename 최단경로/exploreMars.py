# 화성 탐사
import heapq

directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

for _ in range(int(input())):
    n = int(input())
    graph = [list(map(int, input().split())) for _ in range(n)]

    visited = [[False] * n for _ in range(n)]
    visited[0][0] = True
    graph[0][1] += graph[0][0]
    visited[0][1] = True
    graph[1][0] += graph[0][0]
    visited[1][0] = True
    q = []
    heapq.heappush(q, (graph[0][1], (0, 1)))
    heapq.heappush(q, (graph[1][0], (1, 0)))
    while q:
        cnt, idx = heapq.heappop(q)
        x, y = idx
        for dx, dy in directions:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                visited[nx][ny] = True
                graph[nx][ny] += cnt
                heapq.heappush(q, (graph[nx][ny], (nx, ny)))
    print(graph[-1][-1])
        

    
