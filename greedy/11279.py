# 최대 힙
import heapq
q = []
result = []
for _ in range(int(input())):
    check = int(input())
    if check == 0:
        # 최대값 출력
        if len(q) == 0:
            result.append(0)
            continue
        num = heapq.heappop(q) * -1
        result.append(num)
    else :
        # 최대값 입력
        heapq.heappush(q, check * -1)
print()
for r in result:
    print(r)