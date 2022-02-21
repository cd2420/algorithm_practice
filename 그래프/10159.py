# 저울
n = int(input())
graph = [[0] * (n + 1) for _ in range(n+1)]
m = int(input())
for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = -1
for i in range(1, n + 1):
    for j in range(1, n + 1):
        for k in range(1, n + 1):
            if graph[j][i] == 1 and graph[i][k] == 1:
                graph[j][k] = 1
            elif graph[j][i] == -1 and graph[i][k] == -1:
                graph[j][k] = -1
            graph[k][j] = graph[j][k] * -1
for i in range(1, n+1):
    print(graph[i].count(0) - 2)
