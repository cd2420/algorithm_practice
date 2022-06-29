# 병사 배치하기
n = int(input())
soldier = list(map(int, input().split()))
dp = [1] * n
for i in range(1, n):
    for j in range(i-1, -1, -1):
        if soldier[i] < soldier[j]:
            dp[i] = max(dp[i], dp[j] + 1)
        
print(n - max(dp))