# 프로그래머스
# 예상 대진표
def solution(n,a,b):
    answer = 1
    if a > b :
        a, b = b, a
    while a < b:
        if b % 2 == 0 and b - a == 1:
            break
        
        if a % 2 == 0 :
            a //= 2
        else:
            a = a // 2 + 1
            
        if b % 2 == 0 :
            b //= 2
        else:
            b = b // 2 + 1
        
        answer += 1
        
    return answer