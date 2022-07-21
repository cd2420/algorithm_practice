# 프로그래머스
# 야근 지수
import heapq
def solution(n, works):
    answer = 0
    q = []
    for work in works:
        heapq.heappush(q, work * -1)
    while q and n > 0 :
        num = heapq.heappop(q) * -1
        num -= 1
        if num != 0:
            heapq.heappush(q, num * -1)
        n -= 1
    if not q:
        return 0
    else :
        for n in q:
            answer += (n ** 2)
        return answer