# 피보나치 수열
dp = [[] for _ in range(41)]
dp[0] = (1, 0)
dp[1] = (0, 1)
for i in range(2, 41):
    x0, x1 = dp[i-2]
    y0, y1 = dp[i-1]
    dp[i] = (x0 + y0, x1 + y1)
for _ in range(int(input())):
    result = dp[int(input())]
    print(result[0], result[1])
