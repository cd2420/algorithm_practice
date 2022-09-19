
import heapq
from collections import defaultdict

# 최소 스패닝 트리 (최소 신장 트리)
# 크루스칼 알고리즘.
def find_parent(x):
    if x == parent[x]:
        return x
    else :
        a = find_parent(parent[x])
        parent[x] = a
        return a
def union_parent(a, b):
    if a > b:
        parent[a] = b
    else :
        parent[b] = a

V,E = map(int, input().split())
parent = [i for i in range(V+1)]
q = []
for _ in  range(E):
    a,b,c = map(int, input().split())
    heapq.heappush(q, (c, a, b))
result = 0
while q:
    cnt, a, b = heapq.heappop(q)
    a = find_parent(a)
    b = find_parent(b)
    if a == b:
        continue
    result += cnt
    union_parent(a, b)
print(result)

# 프림 알고리즘.
V,E = map(int, input().split())
check = defaultdict(list)
for _ in range(E):
    a,b,c = map(int, input().split())
    check[a].append((c, b))
    check[b].append((c, a))
visited_node = set()
start = 0
for k in check.keys():
    if check[k]:
        start = k
        break
heapq.heapify(check[start]) 
q = check[start]
visited_node.add(start)
result = 0
while q:
    cnt, now = heapq.heappop(q)
    if now in visited_node:
        continue
    visited_node.add(now)
    result += cnt
    for nxt in check[now]:
        heapq.heappush(q, (nxt[0], nxt[1]))
print(result)
