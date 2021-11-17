# ACM craft
from collections import deque

for _ in range(int(input())):
    N, K = map(int, input().split())
    D = list(map(int, input().split()))
    D.insert(0, 0)
    building = [[] for _ in range(N+1)]
    check = [0] * (N+1)
    for i in range(K):
        x, y = map(int, input().split())
        check[y] += 1
        building[x].append(y)
    dp_time = [0] * (N+1)
    q = deque([])
    for i in range(1, N+1):
        if check[i] == 0:
            q.append(i)

    dp = D[:]
    while q:
        x = q.popleft()
        for b in building[x]:
            check[b] -= 1
            dp[b] = max(dp[b], dp[x] + D[b])
            if check[b] == 0:
                q.append(b)
    print(dp[int(input())])
