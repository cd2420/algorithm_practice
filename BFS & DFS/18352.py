# 특정 거리의 도시 찾기
from collections import deque

n, m, k, x = map(int, input().split())
arr = [[] for _ in range(n+1)]
visited = [-1] * (n+1)
for _ in range(m):
    a, b = map(int, input().split())
    arr[a].append(b)
visited[x] = 0
q = deque([])
for i in arr[x]:
    q.append((i, 0))
while q:
    x, cnt = q.popleft()
    if visited[x] != -1:
        continue
    visited[x] = cnt + 1
    for nxt in arr[x]:
        if visited[nxt] == -1:
            q.append((nxt, cnt+1))
is_false = True
for i in range(1, n+1):
    if visited[i] == k:
        print(i)
        is_false = False
if is_false:
    print(-1)