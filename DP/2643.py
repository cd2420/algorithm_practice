# 색종이 올려 놓기
n = int(input())
graph = [sorted(list(map(int, input().split())), reverse=True) for _ in range(n)]
graph.sort(reverse=True)
dp = [1] * n
for i in range(1, n):
    for j in range(i-1, -1, -1):
        if graph[j][1] >= graph[i][1]:
            dp[i] = max(dp[i], dp[j] + 1)
print(max(dp))