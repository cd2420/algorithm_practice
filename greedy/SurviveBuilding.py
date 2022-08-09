# 프로그래머스
# 파괴되지 않은 건물
def solution(board, skill):
    answer = 0
    n = len(board)
    m = len(board[0])
    dp = [[0] * (m+1) for _ in range(n+1)]
    for t, x1, y1, x2, y2, degree in skill:
        if t == 1:
            degree *= -1
        dp[x1][y1] += degree
        dp[x1][y2+1] -= degree
        dp[x2+1][y1] -= degree
        dp[x2+1][y2+1] += degree
    
    for i in range(n+1):
        for j in range(1, m+1):
            dp[i][j] += dp[i][j-1]
    for j in range(m+1):
        for i in range(1, n+1):
            dp[i][j] += dp[i-1][j]
            
    for i in range(n):
        for j in range(m):
            board[i][j] += dp[i][j]
    
    for b in board:
        for _b in b:
            if _b > 0 :
                answer += 1
    
    return answer