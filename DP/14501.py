# 퇴사
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
dp = [0] * n
if arr[-1][0] <= 1 :
    dp[-1] = arr[-1][1]
for i in range(n-2, -1, -1):
    t, p = arr[i]
    if i + t - 1 >= n:
        dp[i] = dp[i+1]
        continue
    if i + t < n:
        dp[i] = max(dp[i+1], arr[i][1] + dp[i+t])
    else :
        dp[i] = max(arr[i][1], dp[i+1])
print(dp[0])