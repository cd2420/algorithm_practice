# 정렬된 배열에서 특정 수의 개수 구하기
from bisect import bisect_left, bisect_right

n,x = map(int, input().split())
nums = list(map(int, input().split()))

check = bisect_right(nums, x) - bisect_left(nums, x)
print(check if check > 0 else -1)