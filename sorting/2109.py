# 순회강연
import heapq
n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
graph.sort(key=lambda x:x[1])
print(graph)
result = []
for i in range(n):
    p, d = graph[i]
    heapq.heappush(result, p)
    
    if len(result) > d:
        heapq.heappop(result)
print(sum(result))
