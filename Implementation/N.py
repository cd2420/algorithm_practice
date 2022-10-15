# 프로그래머스
# N개의 최소공배수
def solution(arr):
    answer = 1
    i = 2
    n = len(arr)
    check = max(arr)
    while i <= check:
        count = 0
        for a in range(n):
            if arr[a] % i == 0 :
                arr[a] //= i
            else :
                count += 1
        if count == n:
            i += 1
            continue
        answer *= i
        
    return answer