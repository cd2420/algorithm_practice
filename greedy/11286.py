# 절댓값 힙
import heapq

arr = []
result = []
for _ in range(int(input())):
    num = int(input())
    if num != 0:
        check = 1
        if num < 0:
            check = -1
            num = abs(num)
        heapq.heappush(arr, (num, check))
    else :
        if arr:
            result1 = heapq.heappop(arr)
            if arr and result1[0] == arr[0][0]:
                result2 = heapq.heappop(arr)
                if result1[0] * result1[1] > result2[0] * result2[1]:
                    heapq.heappush(arr, result1)
                    result.append(result2[0] * result2[1])
                else :
                    heapq.heappush(arr, result2)
                    result.append(result1[0] * result1[1])
            else :
                result.append(result1[0] * result1[1])
        else :
            result.append(0)

for r in result:
    print(r)
