# 호텔
c, n = map(int, input().split())
cities = [list(map(int, input().split())) for _ in range(n)]
dp = [1e9] * (c + 1)
dp[0] = 0

for i in range(1, c+1):
    for cost, person in cities:
        if person >= i:
            dp[i] = min(dp[i], cost)
        else:
            dp[i] = min(dp[i], cost + dp[i - person])
print(dp[-1])
