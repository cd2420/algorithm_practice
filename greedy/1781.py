# 컵라면
import heapq
n = int(input())
ramen = []
q = []
for _ in range(n):
    a, b = map(int, input().split())
    ramen.append((a, b))
ramen.sort(key=lambda x:x[0])
for i in range(n):
    a, b = ramen[i]
    heapq.heappush(q, b)
    while len(q) > a:
        heapq.heappop(q)
print(sum(q))

