# 파도반 수열

for _ in range(int(input())):
    n = int(input())
    if n < 3:
        print(1)
        continue
    dp = [1, 1, 1]
    for i in range(3, n):
        dp.append(dp[i-2] + dp[i-3])
    print(dp[-1])