# 소수의 곱
import heapq

k, n = map(int, input().split())
numbers = list(map(int, input().split()))
q = numbers[:]
count = 0
result = -1
while count < n:
    tmp_result = heapq.heappop(q)
    if tmp_result == result:
        continue
    result = tmp_result
    for num in numbers:
        nr = num * result
        heapq.heappush(q, nr)

    count += 1
print(result)