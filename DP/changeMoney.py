# 프로그래머스
# 거스름돈
def solution(n, money):
    answer = 0
    dp =[[0] * (n+1) for _ in range(len(money) + 1)]
    
    for i in range(1, len(money)+1):
        m = money[i-1]
        dp[i][0] = 1
        for j in range(1, n+1):
            dp[i][j] = dp[i-1][j]
            if j < m:
                continue
            dp[i][j] += dp[i][j-m]

    return dp[-1][-1]