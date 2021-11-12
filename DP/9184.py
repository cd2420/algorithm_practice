# 신나는 함수 실행
dp = [[[0] * 21 for i in range(21)] for _ in range(21)]

for i in range(21):
    for j in range(21):
        dp[0][i][j] = 1
        dp[i][0][j] = 1
        dp[i][j][0] = 1

for a in range(1, 21):
    for b in range(1, 21):
        for c in range(1, 21):
            if a < b and b < c:
                dp[a][b][c] = dp[a][b][c-1] + dp[a][b-1][c-1] - dp[a][b-1][c]
            else:
                dp[a][b][c] = dp[a-1][b][c] + dp[a-1][b-1][c] + \
                    dp[a-1][b][c-1] - dp[a-1][b-1][c-1]
while True:
    a, b, c = map(int, input().split())
    if a == -1 and b == -1 and c == -1:
        break
    result = 0

    if a <= 0 or b <= 0 or c <= 0:
        result = 1
    elif a > 20 or b > 20 or c > 20:
        result = dp[20][20][20]
    else:
        result = dp[a][b][c]
    print('w(%d, %d, %d) = ' % (a, b, c) + str(result))
