# 가장 가까운 공통 조상
import sys
sys.setrecursionlimit(1000000)

def dfs(x, cnt, visited, depth, graph):

    depth[x] = cnt
    visited[x] = True
    for i in graph[x]:
        if visited[i]:
            continue
        dfs(i, cnt + 1, visited, depth, graph)

def lca(x, y, depth, parent):
    
    while depth[x] != depth[y]:
        if depth[x] > depth[y]:
            x = parent[x]
        else :
            y = parent[y]
    
    while x != y:
        x = parent[x]
        y = parent[y]
    return x

result = []
for _ in range(int(input())):
    N = int(input())
    parent = [i for i in range(N+1)]
    depth = [0] * (N+1)
    visited = [False] * (N+1)
    graph = [[] for _ in range(N+1)]
    have_parent = [False] * (N+1)
    for __ in range(N-1):
        a,b = map(int, input().split())
        have_parent[b] = True
        parent[b] = a
        graph[a].append(b)
        graph[b].append(a)
    root = 0
    for i in range(1, N+1):
        if not have_parent[i]:
            root = i
            break
    dfs(root, 0, visited, depth, graph)

    a, b = map(int, input().split())
    result.append(lca(a, b, depth, parent))
for r in result:
    print(r)