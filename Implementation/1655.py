# 가운데를 말해요
import heapq
import sys

input = sys.stdin.readline
N = int(input())
nums = [int(input()) for _ in range(N)]
left = [nums[0] * -1]
right = []
result = [nums[0]]
for i in range(1, N):
    num = nums[i]
    
    if left[0] * -1 >= num:
        left_num = heapq.heappop(left) * -1
        heapq.heappush(right, left_num)
        heapq.heappush(left, num * -1)
    else :
        heapq.heappush(right, num)
    
    if len(left) == len(right):
        if left[0] * -1 >= right[0]:
            left_num = heapq.heappop(left) * -1
            right_num = heapq.heappop(right)
            heapq.heappush(left, right_num * -1)
            heapq.heappush(right, left_num)
    else :
        right_num = heapq.heappop(right)
        heapq.heappush(left, right_num * -1)
    
    result.append(left[0] * -1)

for r in result:
    print(r)

        
        

        
        
