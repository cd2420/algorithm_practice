# 팰린드롬?
import sys
input = sys.stdin.readline
n = int(input().rstrip())
nums = list(map(int, input().split()))
dp = [[False] * n for _ in range(n)]
m = int(input().rstrip())
check = [list(map(int, input().split())) for _ in range(m)]
for i in range(n):
    dp[i][i] = True
for i in range(n-1, -1, -1):
    for j in range(i + 1, n):
        if nums[i] == nums[j]:
            if j - i == 1:
                dp[i][j] = True
            else:
                dp[i][j] = dp[i+1][j-1]
for c_x, c_y in check:
    if dp[c_x-1][c_y-1]:
        print(1)
    else:
        print(0)
