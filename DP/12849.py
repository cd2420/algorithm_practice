# 본대 산책
tree = {
    0 : [1, 2],
    1 : [0, 2, 3],
    2 : [0, 1, 3, 5],
    3 : [1, 2, 4, 5],
    4 : [3, 5, 7],
    5 : [2, 3, 4, 6],
    6 : [5, 7],
    7 : [6, 4]
}

D = int(input())
dp = [[0] * 8 for _ in range(D+1)]

dp[0][0] = 1
for i in range(1, D+1):
    for j in range(8):
        for nxt in tree[j]:
            dp[i][j] += dp[i-1][nxt]
        dp[i][j] %= 1000000007
print(dp[-1][0])
