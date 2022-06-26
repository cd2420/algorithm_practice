# 줄세우기
n = int(input())
person = list(map(int, input().split()))
dp = [0] * (n+1)
for p in person:
    dp[p] = 1
    if p - 1 >= 0:
        dp[p] = max(dp[p], dp[p-1] + 1)
print(n - max(dp))