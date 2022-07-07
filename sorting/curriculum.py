# 커리큘럼
from collections import deque

n = int(input())
lecture_time = [0] * (n+1)
result = [0] * (n+1)
number = [0] * (n+1)
graph = [[] for _ in range(n+1)]
for i in range(n):
    idx = i + 1
    check = list(map(int, input().split()))
    take_time = check.pop(0)
    lecture_time[idx] = take_time
    result[idx] = take_time
    while check[0] != -1:
        prev_lecture = check.pop(0)
        graph[prev_lecture].append(idx)
        number[idx] += 1

check = deque([])
for i in range(1, n+1):
    if number[i] == 0:
        check.append(i)

while check:
    
    lecture = check.popleft()
    for j in graph[lecture]:
        number[j] -= 1
        result[j] = max(result[j], result[lecture] + lecture_time[j])
        if number[j] == 0:
            check.append(j)

for r in result:
    print(r)
