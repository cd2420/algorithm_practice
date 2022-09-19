# 개근상
# dp + dfs
import sys
sys.setrecursionlimit(1000000)
def dfs(day, late, absoluate):
    if late == 2 or absoluate == 3:
        return 0
    if day == n:
        return 1
    if dp[day][late][absoluate] != -1:
        return dp[day][late][absoluate]
    
    attend = (
        dfs(day+1, late, 0)
        + dfs(day+1, late+1, 0)
        + dfs(day+1, late, absoluate + 1)
    )
    dp[day][late][absoluate] = attend
    return attend

n = int(input())
dp = [[[-1, -1, -1] for late in range(2)] for day in range(n)]
print(dfs(0, 0, 0) % 1000000)