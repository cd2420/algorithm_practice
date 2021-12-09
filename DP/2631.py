# 줄세우기
n = int(input())
rows = [int(input()) for _ in range(n)]
dp = [1] * n
for i in range(1, n):
    for j in range(i - 1, -1, -1):
        if rows[i] > rows[j]:
            dp[i] = max(dp[i], dp[j] + 1)
print(n - max(dp))
