# 조 짜기
n = int(input())
students = list(map(int, input().split()))
dp = [0] * n
section_max = [[0] * n for _ in range(n)]

for i in range(n):
    for j in range(i, n):
        if i == j:
            section_max[i][j] = 0
        else:
            section_max[i][j] = max(students[i:j + 1]) - min(students[i:j + 1])
if n > 1:
    dp[1] = abs(students[1] - students[0])

for i in range(2, n):
    dp[i] = max(dp[i], dp[i-1], section_max[0][i])
    for j in range(i - 1, 0, -1):
        dp[i] = max(dp[i], dp[i-1], section_max[j][i] + dp[j-1])
print(dp[-1])
