# 최단 경로
import heapq


def dkstra(start):
    heap = []
    heapq.heappush(heap, (0, start))

    while heap:
        dist, now = heapq.heappop(heap)
        if visited[now] < dist:
            continue
        for next, cost in graph[now]:
            check = dist + cost
            if visited[next] > check:
                visited[next] = check
                heapq.heappush(heap, (check, next))


V, E = map(int, input().split())
start = int(input())
graph = [[] for _ in range(V + 1)]
for i in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
visited = [1e9] * (V + 1)
visited[start] = 0
dkstra(start)
for i in range(1, V + 1):
    if visited[i] == 1e9:
        print('INF')
    else:
        print(visited[i])
