# 트리의 지름
import sys
sys.setrecursionlimit(1000000)


def dfs(start, visited):

    if visited[start] == -1:
        visited[start] = 0
    for next, cost in tree[start]:
        if visited[next] == -1:
            visited[next] = visited[start] + cost
            dfs(next, visited)


n = int(input())
tree = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    a, b, c = map(int, input().split())
    tree[a].append((b, c))
    tree[b].append((a, c))

visited = [-1] * (n+1)
dfs(1, visited)
visited[0] = 0

check_idx = 1
check_num = 0
for i in range(2, n+1):
    if visited[i] > check_num:
        check_num = visited[i]
        check_idx = i

visited = [-1] * (n+1)
dfs(check_idx, visited)
print(max(visited))
