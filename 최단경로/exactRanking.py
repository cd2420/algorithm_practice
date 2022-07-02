# 정확한 순위
n,m = map(int, input().split())
dp = [[1e9] * (n+1) for _ in range(n+1)]
for i in range(1, n+1):
    dp[i][i] = 0
for _ in range(m):
    a, b = map(int, input().split())
    dp[a][b] = -1
    dp[b][a] = 1

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            if dp[i][j] == 1e9 and dp[i][k] != 1e9 and dp[k][j] != 1e9:
                if dp[i][k] == -1 and dp[k][j] == -1:
                    dp[i][j] = -1
                elif dp[i][k] == 1 and dp[k][j] == 1:
                    dp[i][j] = 1
result = 0
for i in range(1, n+1):
    for j in range(1, n+1):
        if dp[i][j] == 1e9:
            break
    else :
        result += 1
print(result)
    
            