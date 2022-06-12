# 방번호
n = int(input())
p = list(map(int, input().split()))
m = int(input())
dp = [-1] * (m+1)
for i in range(1, m+1):
    for num in range(n):
        price = p[num]
        if i >= price:
            if dp[i] == -1:
                dp[i] = num
            dp[i] = max(dp[i], num, dp[i-price] * 10 + num)
print(dp[-1])