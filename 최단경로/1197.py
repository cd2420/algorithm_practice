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


# 크루스칼 알고리즘
def find_parent(x):
    if x == tree[x]:
        return x
    else:
        a = find_parent(tree[x])
        tree[x] = a
        return a


v, e = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(e)]
graph.sort(key=lambda x: x[2])
tree = {}
for i in range(1, v+1):
    tree[i] = i

result = 0
for now, nxt, cost in graph:

    a = find_parent(now)
    b = find_parent(nxt)
    if a == b:
        continue
    else:
        result += cost
        if a > b:
            tree[a] = b
        else:
            tree[b] = a
print(result)
