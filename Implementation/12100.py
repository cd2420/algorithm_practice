# 2048

from copy import deepcopy

def rotation_90(graph):
    size = len(graph)
    result = [[0] * size for _ in range(size)]
    for i in range(size):
        for j in range(size):
            result[j][size-i-1] = graph[i][j]
    return result

def ban_rotation_90(graph):
    size = len(graph)
    result = [[0] * size for _ in range(size)]
    for i in range(size):
        for j in range(size):
            result[size-j-1][i] = graph[i][j]
    return result

def start(dir, cnt, graph):
    global answer
    if cnt == 5:
        answer = max(answer, get_max_num(graph))
        return
    
    tmp_graph = deepcopy(graph)
    
    for _ in range(dir):
        tmp_graph = ban_rotation_90(tmp_graph)
    
    tmp_graph = move_graph(tmp_graph)

    for _ in range(dir):
        tmp_graph = rotation_90(tmp_graph)
    
    for i in range(4):
        start(i, cnt + 1, tmp_graph)

def move_graph(graph):
    size = len(graph)
    tmp_graph = []    

    for g in graph:
        tmp = []
        for i in g:
            if i != 0:
                tmp.append(i)
        tmp += [0] * (size - len(tmp))
        tmp_graph.append(tmp)

    for g in tmp_graph:
        for i in range(1, size):
            if g[i-1] == g[i]:
                g[i-1] *= 2
                g[i] = 0

    result = []
    for g in tmp_graph:
        row = []
        for i in g:
            if i != 0:
                row.append(i)
        row += [0] * (size - len(row))
        result.append(row)
    
    return result

def get_max_num(graph):
    result = -1
    for g in graph:
        result = max(result, max(g))
    return result

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
answer = -1
for i in range(4):
    start(i, 0, graph)
print(answer)