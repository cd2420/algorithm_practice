# 1,2,3 더하기 6
dp = [0] * 100001
dp[1] = 1
dp[2] = 2
dp[3] = 2
dp[4] = 3
dp[5] = 3
dp[6] = 6
for i in range(7, 100001):
    dp[i] = (dp[i - 6] + dp[i - 4] + dp[i - 2]) % 1000000009

for _ in range(int(input())):
    n = int(input())
    print(dp[n])
