# 사회망 서비스(sns)
import sys
sys.setrecursionlimit(10 ** 9)
input = sys.stdin.readline
def dfs(x):
    if visited[x]:
        return
    visited[x] = True
    dp[x][0] = 1
    for nxt in arr[x]:
        if not visited[nxt]:
            dfs(nxt)
            dp[x][0] += min(dp[nxt][0], dp[nxt][1])
            dp[x][1] += dp[nxt][0]

n = int(input())
arr = [[] for _ in range(n+1)]
for _ in range(n-1):
    a,b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)
visited = [False] * (n+1)
dp = [[0,0] for _ in range(n+1)]
dfs(1)
print(min(dp[1]))
