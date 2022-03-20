# 원판 돌리기
from collections import deque


def clock(arr, cnt):
    for _ in range(cnt):
        arr.appendleft(arr.pop())


def ban_clock(arr, cnt):
    for _ in range(cnt):
        arr.append(arr.popleft())


def check_graph():

    resolve_g = set()
    for i in range(1, N+1):
        tmp_g = list(set(graph[i]))
        if len(tmp_g) == 1 and tmp_g[0] == 0:
            continue
        else:
            find_same_num(graph[i], i, resolve_g)
    if len(resolve_g) > 0:
        while resolve_g:
            circle, idx = resolve_g.pop()
            graph[circle][idx] = 0
    else:
        total_sum = 0
        cnt = 0
        for i in range(1, N + 1):
            for j in range(M):
                if graph[i][j] != 0:
                    total_sum += graph[i][j]
                    cnt += 1
        if cnt:
            avg = total_sum / cnt
            for i in range(1, N + 1):
                for j in range(M):
                    if graph[i][j] != 0:
                        if graph[i][j] > avg:
                            graph[i][j] -= 1
                        elif graph[i][j] < avg:
                            graph[i][j] += 1


def find_same_num(g, now, resolve_g):

    prev_circle = now - 1
    nxt_circle = now + 1
    for i in range(M):
        now_prev = i - 1 if i - 1 >= 0 else M - 1
        now_nxt = i + 1 if i + 1 < M else 0
        if g[i] and g[i] == g[now_prev]:
            resolve_g.add((now, i))
            resolve_g.add((now, now_prev))
        if g[i] and g[i] == g[now_nxt]:
            resolve_g.add((now, i))
            resolve_g.add((now, now_nxt))
        if g[i] and prev_circle > 0 and graph[prev_circle][i] == g[i]:
            resolve_g.add((prev_circle, i))
            resolve_g.add((now, i))
        if g[i] and nxt_circle < N+1 and graph[nxt_circle][i] == g[i]:
            resolve_g.add((nxt_circle, i))
            resolve_g.add((now, i))


N, M, T = map(int, input().split())
graph = [deque(list(map(int, input().split()))) for _ in range(N)]
graph.insert(0, [])
test_case = [list(map(int, input().split())) for _ in range(T)]
for x, d, k in test_case:
    for i in range(x, N+1, x):
        if d == 0:
            clock(graph[i], k)
        else:
            ban_clock(graph[i], k)
    check_graph()
result = 0
for g in range(1, N+1):
    result += sum(graph[g])
print(result)
