# 볼링공 고르기

n,m = map(int, input().split())
dp = [0] * (m+1)
balls = list(map(int, input().split()))
for b in balls:
    dp[b] += 1
result = 0
for b in range(m+1):
    ball = dp[b]
    n -= ball
    result += n * ball
print(result)