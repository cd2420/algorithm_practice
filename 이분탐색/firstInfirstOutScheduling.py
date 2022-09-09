# 프로그래머스
# 선입 선출 스케줄링
def solution(n, cores):
    answer = 0
    if n <= len(cores):
        return n
    n -= len(cores)
    
    time = 1e9
    start = 1
    end = 10000 * 10000
    while start <= end:
        mid = (start + end) // 2
        cnt = 0
        for c in cores:
            cnt += mid // c
        if cnt >= n:
            time = min(time, mid)
            end = mid - 1
        else :
            start = mid + 1

    for c in cores:
        n -= (time-1) // c
        
    for c in range(len(cores)):
        if time % cores[c] == 0:
            n -= 1
            if n == 0:
                answer = c+1
                break
    return answer