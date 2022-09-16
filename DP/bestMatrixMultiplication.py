# 프로그래머스
# 최적의 행렬 곱셈
def solution(matrix_sizes):
    answer = 0
    n = len(matrix_sizes)
    dp = [[1e9] * n for _ in range(n)]
    for i in range(n):
        dp[i][i] = 0
    for size in range(1, n):
        for i in range(n-1):
            j = i + size
            if j >= n:
                break
            for sep in range(i, j):
                dp[i][j] = min(dp[i][j], dp[i][sep] + dp[sep+1][j] + matrix_sizes[i][0] * matrix_sizes[sep][1] * matrix_sizes[j][1])
    return dp[0][-1]