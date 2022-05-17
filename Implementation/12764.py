# 싸지방에 간 준하
from collections import defaultdict
import heapq

n = int(input())
peoples = [list(map(int, input().split())) for _ in range(n)]
peoples.sort(reverse=True)
result = defaultdict(int)
q = []
idx_q = []
while peoples:
    s, e = peoples.pop()
    while q:
        t_e, t_idx = heapq.heappop(q)
        if s > t_e:
            heapq.heappush(idx_q, t_idx)
        else :
            heapq.heappush(q, (t_e, t_idx))
            break
    check_idx = len(q) + 1
    if idx_q:
        check_idx = heapq.heappop(idx_q)
    result[check_idx] += 1
    heapq.heappush(q, (e, check_idx))
print(len(result))
result2 = ''
for val in result.values():
    result2 += str(val) + ' '
print(result2.rstrip())