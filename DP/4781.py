# 사탕가게
import sys
input = sys.stdin.readline
while True:
    n, money = input().split()
    n = int(n)
    if n == 0:
        break
    money = round(float(money) * 100)

    dp = [0] * (money + 1)
    for i in range(1, n+1):
        c, p = input().split()
        c = int(c)
        p = round(float(p) * 100)
        for j in range(p, money + 1):
            dp[j] = max(dp[j], dp[j - p] + c)
    print(dp[money])
