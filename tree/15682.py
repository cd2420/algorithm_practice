# 트리와 쿼리

import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

def dfs(root, cnt):

    depth[root] = cnt
    for i in graph[root]:
        if depth[i] == -1:
            dfs(i, cnt + 1)

def dfs2(root, check):
    if depth[root] == check:
        return 1

    for i in graph[root]:
        if depth[root] < depth[i]:
            dfs2(i, check)
            dp[root] += dp[i]
    
n, r, q = map(int, input().split())
graph = [[] for _ in range(n+1)]
print_result = []
for _ in range(n-1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

depth = [-1] * (n+1)
dp = [1] * (n+1)
dfs(r, 0)
check = max(depth)
dfs2(r, check)
for _ in range(q):
    target = int(input())
    print_result.append(dp[target])
for r in print_result:
    print(r)