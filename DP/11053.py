# 가장 긴 증가하는 부분 수열
N = int(input())
A = list(map(int, input().split()))
dp = [1] * N
for i in range(N):
    for j in range(i, -1, -1):
        if A[i] > A[j]:
            dp[i] = max(dp[i], dp[j] + 1)
print(max(dp))
