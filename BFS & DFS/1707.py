# 이분 그래프
import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)


def dfs(start, now, graph, state):
    if state[start] != 0:
        return
    state[start] = now
    for nxt in graph[start]:
        if state[start] == state[nxt]:
            return False
        rst = dfs(nxt, now * -1, graph, state)
        if rst == False:
            return False


for _ in range(int(input())):
    v, e = map(int, input().split())
    graph = [[] for _ in range(v + 1)]
    for __ in range(e):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    state = [0] * (v + 1)
    is_no = False
    for i in range(1, v + 1):
        if dfs(i, 1, graph, state) == False:
            is_no = True
            break
    if is_no:
        print('NO')
    else:
        print('YES')
