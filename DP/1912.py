# 연속합
n = int(input())
nums = list(map(int, input().split()))
dp = [0] * n
dp[0] = nums[0]
check = nums[0]
for i in range(1, n):
    check += nums[i]
    if nums[i] > check:
        check = nums[i]
    dp[i] = max(dp[i-1], check)
print(dp[-1])
