# 부분 합
N, S = map(int, input().split())
nums = list(map(int, input().split()))

start = 0
end = 0
nums_sum = nums[start]
result = 1e9
while start <= end:

    if nums_sum < S:
        end += 1
        if end >= N:
            break
        nums_sum += nums[end]
    else:
        if result > end - start + 1:
            result = end - start + 1
        if result == 1:
            break
        nums_sum -= nums[start]
        start += 1
        if start >= N:
            break
if result == 1e9:
    print(0)
else:
    print(result)
