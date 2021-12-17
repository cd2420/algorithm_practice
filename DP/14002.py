# 가장 긴 증가하는 부분 수열 4
n = int(input())
nums = list(map(int, input().split()))
max_count = 1
result_num = [nums[0]]
dp = [[1, []] for _ in range(n)]
dp[0][1].append(nums[0])


for i in range(1, n):
    result_list = []
    check_max_num = 1
    for j in range(i-1, -1, -1):
        if nums[i] > nums[j]:
            dp[i][0] = max(dp[i][0], dp[j][0] + 1)
            if dp[i][0] > check_max_num:
                check_max_num = dp[i][0]
                result_list = dp[j][1][:]
    dp[i][1].extend(result_list)
    dp[i][1].append(nums[i])

result_num, result_list = max(dp, key=lambda x: x[0])
print(result_num)
for r in result_list:
    print(r, end=' ')
