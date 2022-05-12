# 커플 만들기
n, m = map(int, input().split())
men = list(map(int, input().split()))
women = list(map(int, input().split()))

men.sort()
men.insert(0, 0)
women.sort()
women.insert(0, 0)

dp = [[0] * (m+1) for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, m+1):
        if i == j:
            dp[i][j] = dp[i-1][j-1] + abs(men[i] - women[j])
        elif i > j:
            dp[i][j] = min(dp[i-1][j], dp[i-1][j-1] + abs(men[i] - women[j]))
        else :
            dp[i][j] = min(dp[i][j-1], dp[i-1][j-1] + abs(men[i] - women[j]))

print(dp[-1][-1])
            


