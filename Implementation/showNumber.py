# 프로그래머스
# 숫자의 표현
def solution(n):
    answer = 1
    a = n
    if n % 2 != 0 :
        a = n // 2 + 1
    else :
        a = n // 2 - 1
    
    for i in range(a, 0, -1):
        check = i
        for j in range(i-1, 0, -1):
            check += j 
            if check == n:
                answer += 1 
                break
            if check > n:
                break
        
    return answer