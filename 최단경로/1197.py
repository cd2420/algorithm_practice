# 최소 스패닝 트리 (최소 신장 트리)
# 크루스칼 알고리즘.
def find_parent(x):
    if parent[x] == x:
        return x
    else :
        a = find_parent(parent[x])
        parent[x] = a
        return a

def union_parent(a, b):
    a = find_parent(a)
    b = find_parent(b)

    if a > b:
        parent[a] = b
    else :
        parent[b] = a

V, E = map(int, input().split())
parent = [i for i in range(V+1)]
graph = []
for _ in range(E):
    a, b, c = map(int, input().split())
    graph.append((c, a, b))
graph.sort()
result = 0
for cnt, a, b in graph:
    a = find_parent(a)
    b = find_parent(b)
    if a == b:
        continue
    result += cnt
    union_parent(a, b)
print(result)

# 프림 알고리즘.
from collections import defaultdict
import heapq

V,E = map(int, input().split())
graph = defaultdict(list)
for _ in range(E):
    a,b,c = map(int, input().split())
    graph[a].append((c, a, b))
    graph[b].append((c, b, a))

connected_node = set()
connected_node.add(1)
candidate_edge_list = graph[1]
heapq.heapify(candidate_edge_list)
result = 0
while candidate_edge_list:
    cnt, a, b = heapq.heappop(candidate_edge_list)
    if b not in connected_node:
        connected_node.add(b)
        result += cnt
        for edge in graph[b]:
            if edge[2] not in connected_node:
                heapq.heappush(candidate_edge_list, edge)
print(result)