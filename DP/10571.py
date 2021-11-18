# 다이아몬드
import sys
input = sys.stdin.readline

for _ in range(int(input())):
    N = int(input())
    diamonds = [list(map(float, input().split())) for i in range(N)]
    dp = [1] * N
    for i in range(N):
        for j in range(i-1, -1, -1):
            if diamonds[i][0] > diamonds[j][0] and diamonds[i][1] < diamonds[j][1]:
                dp[i] = max(dp[i], dp[j] + 1)
    print(max(dp))
