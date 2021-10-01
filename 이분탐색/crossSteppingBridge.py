# 징검다리 건너기
def solution(stones, k):
    answer = 0

    start = min(stones)
    end = max(stones)
    result = min(stones)
    while start <= end:
        mid = (start + end) // 2

        cnt = 0
        for stone in stones:
            if stone - mid <= 0:
                cnt += 1
            else:
                cnt = 0
            if cnt >= k:
                break

        if cnt >= k:
            result = mid
            end = mid - 1
        else:
            start = mid + 1
    answer = result
    return answer
