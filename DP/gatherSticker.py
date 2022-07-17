# 프로그래머스
# 스티커 모으기
def solution(sticker):
    n = len(sticker)
    dp = [[0, 0] for _ in range(n)]
    dp[0][0] = sticker[0]
    if n == 1:
        return sticker[0]
    
    # 상황 1. 첫번째 무조건 뗄 때.
    dp[1][0] = sticker[0]
    dp[1][1] = 0
    for i in range(2, n-1):
        if i-1 == dp[i-1][1]:
            if dp[i-2][0] + sticker[i] > dp[i-1][0]:
                dp[i][0] = dp[i-2][0] + sticker[i]
                dp[i][1] = i
            else :
                dp[i][1] = dp[i-1][1]
                dp[i][0] = dp[i-1][0]
        else :
            dp[i][0] = dp[i-1][0] + sticker[i]
            dp[i][1] = i
    check1 = dp[-2][0]
    
    # 상황 2. 첫번째 무조건 안 뗄 때.
    dp = [[0, 0] for _ in range(n)]
    dp[1][0] = sticker[1]
    dp[1][1] = 1
    if n == 2:
        return max(sticker[0], sticker[1])

    for i in range(2, n):
        if i-1 == dp[i-1][1]:
            if dp[i-2][0] + sticker[i] > dp[i-1][0]:
                dp[i][0] = dp[i-2][0] + sticker[i]
                dp[i][1] = i
            else :
                dp[i][1] = dp[i-1][1]
                dp[i][0] = dp[i-1][0]
        else :
            dp[i][0] = dp[i-1][0] + sticker[i]
            dp[i][1] = i
    check2 = dp[-1][0]
    answer = max(check1, check2)            
    return answer