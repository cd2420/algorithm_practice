# 과제
import heapq

n = int(input())
check = [list(map(int, input().split())) for _ in range(n)]
check.sort()
q = []
while check:
    d, w = check.pop(0)
    if d <= len(q):
        heapq.heappop(q)
    heapq.heappush(q, (w))
print(sum(q))
    
