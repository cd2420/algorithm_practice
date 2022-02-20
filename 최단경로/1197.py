# 최소 스패닝 트리 (최소 신장 트리)

# 프림 알고리즘.
import heapq

v, e = map(int, input().split())
graph = [[] for _ in range(v + 1)]
for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a].append((c, b))
    graph[b].append((c, a))
visited = [False] * (v + 1)
q = [(0, 1)]
result = 0
while q:
    cost, x = heapq.heappop(q)
    if visited[x]:
        continue
    visited[x] = True

    result += cost
    for i in graph[x]:
        if not visited[i[1]]:
            heapq.heappush(q, (i[0], i[1]))
print(result)
