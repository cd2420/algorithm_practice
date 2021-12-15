# 연속합 2
n = int(input())
nums = list(map(int, input().split()))
dp = [[0, 0, 0] for _ in range(n)]
dp[0][0] = nums[0]
result = nums[0]
for i in range(1, n):
    dp[i][0] = nums[i]  # 자기자신(숫자)
    dp[i][1] = max(dp[i-1][0], dp[i-1][1], dp[i-1][2]) + \
        nums[i]  # 자기자신을 포함한 수열중 최대값
    dp[i][2] = max(dp[i-1][0], dp[i-1][2] + dp[i-1][0])  # 자기자신을 제외한 수열중 최대값
    if max(dp[i]) > result:
        result = max(dp[i])
print(result)
