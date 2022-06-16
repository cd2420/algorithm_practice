# 강의실 배정
import heapq

n = int(input())
lst = [list(map(int, input().split())) for _ in range(n)]
lst.sort()
q = []
for i in lst:
    if q  and q[0][0] <= i[0]:
        heapq.heappop(q)
    heapq.heappush(q, (i[1], i[0]))
print(len(q))