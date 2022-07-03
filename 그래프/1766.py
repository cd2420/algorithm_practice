# 문제집
import heapq
import sys

n, m = map(int, input().split())

child = [[] for _ in range(n+1)]
parent = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    child[b].append(a)
    parent[a].append(b)
if n == 1:
    print(1)
    sys.exit(0)
start = []
for i in range(1, n+1):
    if not child[i]:
        start.append(i)

result = []
while start:
    s = heapq.heappop(start)
    result.append(s)
    for p in parent[s]:
        child[p].remove(s)
        if not child[p]:
            heapq.heappush(start, p)
for i in range(len(result) - 1):
    print(result[i], end = ' ')
print(result[-1])