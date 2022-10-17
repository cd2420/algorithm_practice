# 프로그래머스
# 멀리뛰기

def solution(n):
    answer = 0
    dp = [0] * (n+1)
    dp[1] = 1
    if n > 1 :
        dp[2] = 2
    for i in range(3, n+1):
        dp[i] = dp[i-1] + dp[i-2]
    answer = dp[-1] % 1234567
    return answer