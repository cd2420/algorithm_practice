# 트리
import sys
input = sys.stdin.readline


def dfs(start, parent, visited):
    if visited[start]:
        return False
    visited[start] = True
    for next in graph[start]:

        if next == parent:
            continue

        if visited[next]:
            return False

        if dfs(next, start, visited):
            continue
        else:
            return False

    return True


case = 1
while True:
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break
    graph = [[] for _ in range(n + 1)]
    for _ in range(1, m+1):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    visited = [False] * (n + 1)
    result = 0
    for i in range(1, n + 1):
        if dfs(i, None, visited):
            result += 1

    if result == 0:
        print(f"Case {case}: No trees.")
    elif result == 1:
        print(f"Case {case}: There is one tree.")
    else:
        print(f"Case {case}: A forest of {result} trees.")
    case += 1
