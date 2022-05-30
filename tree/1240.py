# 노드사이의 거리
n,m = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(n-1):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))
result = []
for _ in range(m):
    a, b = map(int, input().split())
    visited = [False] * (n+1)
    q = [(a, 0)]
    while q:
        now, dist = q.pop(0)
        if now == b:
            result.append(dist)
            break
        if visited[now]:
            continue
        visited[now] = True
        for i in graph[now]:
            nxt, val = i
            if visited[nxt]:
                continue
            q.append((nxt, dist+val))

for r in result:
    print(r)