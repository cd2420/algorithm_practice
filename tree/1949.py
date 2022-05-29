# 우수 마을
import sys
sys.setrecursionlimit(1000000)
def dfs(x):
    if visited[x]:
        return
    visited[x] = True
    dp[x][1] = towns[x]
    for i in arr[x]:
        if not visited[i]:
            dfs(i)
            dp[x][0] += max(dp[i][1], dp[i][0])
            dp[x][1] += dp[i][0]

n = int(input())
towns = list(map(int, input().split()))
towns.insert(0, 0)
arr = [[] for _ in range(n+1)]
for _ in range(n-1):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)

dp = [[0, 0] for _ in range(n+1)]
visited = [False] * (n+1)
dfs(1)
print(max(dp[1]))