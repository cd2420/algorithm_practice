# 경사로

def check(graph, x, dir):
    if len(set(graph)) == 1:
        return True

    for j in range(n-1):
        tmp_idx = []
        if graph[j] - graph[j+1] == -1:
            lst = j - l
            if lst < -1:
                return False
            for k in range(j, lst, -1):
                if check_slide[x][k][dir] == -1 and graph[j] == graph[k]:
                    tmp_idx.append(k)
        elif graph[j] - graph[j+1] == 1:
            lst = j + l + 1
            if lst > n:
                return False
            for k in range(j + 1, lst):
                if check_slide[x][k][dir] == -1 and graph[j + 1] == graph[k]:
                    tmp_idx.append(k)
        elif graph[j] != graph[j+1]:
            return False
        else:
            continue

        if len(tmp_idx) == l:
            for idx in tmp_idx:
                check_slide[x][idx][dir] = 1
            continue
        else:
            return False

    return True


n, l = map(int, input().split())
row_graph = [list(map(int, input().split())) for _ in range(n)]
col_graph = []
for i in range(n):
    g = []
    for j in range(n):
        g.append(row_graph[j][i])
    col_graph.append(g)


check_slide = [[[-1, -1] for __ in range(n)] for _ in range(n)]
result = 0
for i in range(n):
    if check(row_graph[i], i, 0):
        result += 1
    if check(col_graph[i], i, 1):
        result += 1
print(result)
