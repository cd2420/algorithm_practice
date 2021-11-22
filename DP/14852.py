# 타일 채우기 3
import sys
input = sys.stdin.readline

n = int(input())
dp = [[0, 0, 0, 0, 0] for _ in range(n)]

dp[0] = [1, 0, 1, 0, 0]
if n > 1:
    dp[1] = [2, 1, 2, 1, 1]
for i in range(2, n):
    dp_1 = sum(dp[i-1]) % 1000000007
    dp_2 = sum(dp[i-2]) % 1000000007
    dp[i] = [dp_1, dp_2, dp_1, dp_2 + dp[i-1][3], dp_2 + dp[i-1][4]]
print(sum(dp[-1]) % 1000000007)
