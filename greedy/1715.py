# 카드 정렬하기
import heapq
n = int(input())
q = []
for _ in range(n):
    num = int(input())
    heapq.heappush(q, num)
result = 0
while q:
    num1 = heapq.heappop(q)
    if q:
        num2 = heapq.heappop(q)
        result += num1 + num2
        heapq.heappush(q, num1 + num2)
    else :
        break
        
print(result)
    