# 프로그래머스
# 점프와 순간이동
def solution(n):
    ans = 0
    
    while n != 0:
        if n % 2 != 0 :
            ans += 1
        n //= 2

    return ans