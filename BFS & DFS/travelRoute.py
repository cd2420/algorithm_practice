# 프로그래머스
# 여행경로
from collections import defaultdict
def solution(tickets):
    result = len(tickets) + 1
    trip = defaultdict(list)
    for a,b in tickets:
        trip[a].append(b)
        trip[a].sort(reverse=True)
    stack = ["ICN"]

    tmp_answer = []
    while stack:
        now = stack[-1]
        if not trip[now]:
            tmp_answer.append(stack.pop())
        else :
            nxt = trip[now].pop()
            stack.append(nxt)
    answer = tmp_answer[::-1]
    return answer