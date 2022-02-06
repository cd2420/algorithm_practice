# 트리의 부모 찾기
import sys
sys.setrecursionlimit(100000)


def dfs(start):
    if visited[start]:
        return
    visited[start] = True
    for next in tree[start]:
        if not visited[next]:
            parent[next] = start
            dfs(next)


n = int(input())
tree = {}
parent = {}
for i in range(1, n+1):
    tree[i] = []
    parent[i] = i
for _ in range(n - 1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

visited = [False] * (n + 1)
dfs(1)
result = list(parent.values())
for i in range(1, len(result)):
    print(result[i])
