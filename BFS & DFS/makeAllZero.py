# 프로그래머스
# 모두 0으로 만들기
import sys
sys.setrecursionlimit(1000000)

def dfs(graph, i, visited, cnt, a):
    global answer
    for nxt in graph[i]:
        if not visited[nxt]:
            visited[nxt] = True
            a[i] += dfs(graph, nxt, visited, cnt, a)
    answer += abs(a[i])
    return a[i]
            
    

def solution(a, edges):
    global answer
    answer = 0
    if sum(a) != 0 :
        return -1
    graph = [[] for _ in range(len(a))]
    for edge in edges:
        x, y = edge
        graph[x].append(y)
        graph[y].append(x)

    visited = [False] * len(a)
    visited[0] = True
    dfs(graph, 0, visited, 0, a)
    return answer