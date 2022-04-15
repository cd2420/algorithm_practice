# 배열 돌리기 4
from copy import deepcopy
from itertools import permutations

def extract(tmp, start, end, n):
    tmp_graph = []
    for i in range(start[0], end[0]+1):
        tmp_row = []
        for j in range(start[1], end[1] + 1):
            tmp_row.append(tmp[i][j])
        tmp_graph.append(tmp_row)

    return_data = rotate(tmp_graph, n)

    for i in range(start[0], end[0]+1):
        for j in range(start[1], end[1] + 1):
            tmp[i][j] = return_data[i-start[0]][j-start[1]]


def rotate(tmp_graph, n):
    result_graph = deepcopy(tmp_graph)
    for i in range(n):
        for j in range(i, n - i - 1):
            result_graph[i][j+1] = tmp_graph[i][j]

        for j in range(i, n - i - 1):
            result_graph[j+1][n-i-1] = tmp_graph[j][n-i-1]
        
        for j in range(n - i - 1, i, -1):
            result_graph[n-i-1][j-1] = tmp_graph[n-i-1][j]

        for j in range(n - i - 1, i, -1):
            result_graph[j-1][i] = tmp_graph[j][i]
    return result_graph

N, M, K = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
calcul = []
order = []
for _ in range(K):
    r, c, s = map(int, input().split())
    calcul.append((r, c, s))
for i in permutations(range(K), K):
    order.append(i)

result = 1e9
for o in order:
    tmp = deepcopy(graph)
    for i in o:
        r, c, s = calcul[i]
        s_x, s_y = r-s-1, c-s-1
        e_x, e_y = r+s-1, c+s-1
        extract(tmp, (s_x, s_y), (e_x, e_y), e_x - s_x + 1)
    for t in tmp:
        result = min(result, sum(t))
print(result)