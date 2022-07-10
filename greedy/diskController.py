# 프로그래머스
# 디스크 컨트롤러
import heapq
def solution(jobs):
    
    size = len(jobs)
    n = 0
    start = 0
    answer = 0
    while n < size:
        q = []
        for i in range(len(jobs)):
            job = jobs[i]
            if job[0] <= start:
                heapq.heappush(q, (job[1], job[0], i))
        
        if q and start >= q[0][1]:
            now = heapq.heappop(q)
            start += now[0]
            answer += start - now[1]
            n += 1
            jobs.pop(now[2])
        else:
            start += 1
    return answer // n
solution([[10, 10], [30, 10], [50, 2], [51, 2]])