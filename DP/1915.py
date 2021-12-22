# 가장 큰 정사각형
n, m = map(int, input().split())
graph = [list(map(int, list(input()))) for _ in range(n)]

for i in range(1, n):
    for j in range(1, m):
        if graph[i][j] == 1:
            graph[i][j] = min(graph[i-1][j], graph[i]
                              [j-1], graph[i-1][j-1]) + 1

result = -1
for g in graph:
    result = max(result, max(g))

print(result * result)
