# 중량 제한
from collections import deque


def check(visited, weight, dept):
    visited[dept] = True
    q = deque([dept])
    while q:
        a = q.popleft()
        for i in bridges[a]:
            _next, check = i
            if not visited[_next] and check >= weight:
                visited[_next] = True
                q.append(_next)


n, m = map(int, input().split())
bridges = [[] for _ in range(n + 1)]
start = 1
end = -1
result = 1
for _ in range(m):
    a, b, c = map(int, input().split())
    if c > end:
        end = c
    bridges[a].append((b, c))
    bridges[b].append((a, c))
dept, ariv = map(int, input().split())

while start <= end:
    mid = (start + end) // 2
    visited = [False] * (n + 1)
    check(visited, mid, dept)
    if visited[ariv]:
        result = mid
        start = mid + 1
    else:
        end = mid - 1
print(result)
