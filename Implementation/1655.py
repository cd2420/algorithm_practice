# 가운데를 말해요 (다시)
import heapq
import sys
input = sys.stdin.readline
n = int(input())
left = []
right = []
result = []
for _ in range(n):
    num = int(input())
    if len(left) == len(right):
        heapq.heappush(left, num * -1)
    else :
        heapq.heappush(right, num)
    if right and left[0] * -1 > right[0]:
        left_num = heapq.heappop(left) * -1
        right_num = heapq.heappop(right)
        heapq.heappush(right, left_num)
        heapq.heappush(left, right_num * -1)
    result.append(left[0] * -1)
for r in result:
    print(r)


    
