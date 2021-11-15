# 가장 큰 증가 부분 수열
N = int(input())
A = list(map(int, input().split()))
dp = A[:]
for i in range(1, N):
    for j in range(i - 1, -1, -1):
        if A[j] < A[i]:
            dp[i] = max(dp[i], dp[j] + A[i])
print(max(dp))
