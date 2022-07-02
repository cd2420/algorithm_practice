# 어두운 길
import heapq
n, m = map(int, input().split())

towns = [i for i in range(n)]
graph = [[] for _ in range(n)]
visited = [False] * n
total = 0
for _ in range(m):
    a,b,c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))
    total += c
q = []
heapq.heappush(q, (0, 0))
result = 0
while q:
    cnt, x = heapq.heappop(q)
    if visited[x]:
        continue
    visited[x] = True
    result += cnt
    for i in graph[x]:
        nxt, val = i
        if not visited[nxt]:
            heapq.heappush(q, (val, nxt))

print(total - result)