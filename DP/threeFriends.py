# 삼총사
def solution(number):
    answer = 0
    n = len(number)
    dp =[[[-1] * n for _ in range(n)] for __ in range(n)]
    visited = [[[False] * n for _ in range(n)] for __ in range(n)]
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            for k in range(n):
                if i == k or j == k:
                    continue
                dp[i][j][k] = number[i] + number[j] + number[k]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                if dp[i][j][k] == 0 and not visited[i][j][k]:
                    visited[i][j][k] = True
                    visited[i][k][j] = True
                    visited[j][i][k] = True
                    visited[j][k][i] = True
                    visited[k][j][i] = True
                    visited[k][i][j] = True
                    answer += 1
    return answer