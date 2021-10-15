def solution(n, times):
    answer = 0

    times.sort()
    start = 0
    result = 0
    end = n * times[-1]

    while start <= end:
        mid = (start + end) // 2
        check = 0
        for time in times:
            time_client = mid // time
            if time_client == 0:
                break
            else:
                check += time_client
        if check >= n:
            result = mid
            end = mid - 1
        else:
            start = mid + 1
    answer = result
    return answer
