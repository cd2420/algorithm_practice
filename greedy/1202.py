# 보석 도둑
import heapq
N, K = map(int, input().split())
jewelry = [list(map(int, input().split())) for _ in range(N)]
jewelry.sort(key=lambda x:x[0] , reverse=True)
bags = [int(input()) for _ in range(K)]
bags.sort()
arr = []
result = 0
for b in bags:
    while jewelry and jewelry[-1][0] <= b:
        m, v = jewelry.pop()
        heapq.heappush(arr, v * -1)
    if arr:
        result += heapq.heappop(arr) * -1
print(result)
