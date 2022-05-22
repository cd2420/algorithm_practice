# 파일 합치기3
import sys
import heapq
input = sys.stdin.readline
for _ in range(int(input())):
    K = int(input())
    nums = list(map(int, input().split()))
    heapq.heapify(nums)
    result = 0
    while nums:
        num1 = heapq.heappop(nums)
        if nums:
            num2 = heapq.heappop(nums)
            check = num1 + num2
            result += check
            heapq.heappush(nums, check)

    print(result)