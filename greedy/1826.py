# 연료 채우기
import heapq

n = int(input())
oils = [list(map(int, input().split())) for _ in range(n)]
oils.sort(reverse=True)
l, p = map(int, input().split())
q = []
result = 0
while p < l:
    while oils and oils[-1][0] <= p:
        a, b = oils.pop()
        heapq.heappush(q, (-b, a))
    if not q :
        break
    oil, s = heapq.heappop(q)
    p += oil * -1
    result += 1
if p < l:
    print(-1)
else :
    print(result)



