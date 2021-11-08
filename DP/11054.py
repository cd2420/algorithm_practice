# 가장 긴 바이토닉 부분 수열
N = int(input())
A = list(map(int, input().split()))
dp = [1] * N
dp_desc = [0] * N
result = [0] * N

for i in range(1, N):
    for j in range(i - 1, -1, -1):
        if A[i] > A[j]:
            dp[i] = max(dp[i], dp[j] + 1)

for i in range(N - 1, -1, -1):
    for j in range(i, N):
        if A[i] > A[j]:
            dp_desc[i] = max(dp_desc[i], dp_desc[j] + 1)

for i in range(N):
    result[i] = dp[i] + dp_desc[i]

print(max(result))
