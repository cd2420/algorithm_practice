# 최소 회의실 개수
import heapq


N = int(input())
meetings = [list(map(int, input().split())) for _ in range(N)]
meetings.sort()
q = []
heapq.heappush(q, meetings[0][1])
for i in range(1, N):
    st, ed = meetings[i]
    if st >= q[0]:
        heapq.heappop(q)
    heapq.heappush(q, ed)

print(len(q))