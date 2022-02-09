# 트리의 지름
def dfs(start, visited, cost):
    visited[start] = cost

    for next, tmp_cost in tree[start]:
        if visited[next] == -1:
            dfs(next, visited, cost + tmp_cost)


v = int(input())
tree = {}
for i in range(1, v+1):
    tree[i] = []
for i in range(v):
    check = list(map(int, input().split()))
    end = len(check) - 1
    for j in range(1, end - 1, 2):
        tree[check[0]].append((check[j], check[j+1]))

visited = [-1] * (v + 1)
dfs(1, visited, 0)

check = visited[1]
next = 1
for i in range(2, v + 1):
    if check < visited[i]:
        next = i
        check = visited[i]

visited = [-1] * (v + 1)
dfs(next, visited, 0)
print(max(visited))
