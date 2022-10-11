# 프로그래머스
# 다음 큰 숫자

def getOne(n):
    cnt = 0
    while n > 1:
        if n % 2 == 1:
            cnt += 1
        n //= 2
    if n == 1:
        cnt += 1
    return cnt

def solution(n):
    answer = n + 1
    check_1 = getOne(n)
    while True:
        if getOne(answer) != check_1:
            answer += 1
        else:
            break
        
    return answer
