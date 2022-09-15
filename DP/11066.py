# 파일 합치기
import sys
input = sys.stdin.readline
for _ in range(int(input())):
    k = int(input())
    files = list(map(int, input().split()))
    dp = [[1e9] * k for _ in range(k)]
    for i in range(k):
        dp[i][i] = 0
    total_sum = [[0] * k for _ in range(k)]
    for i in range(k):
        for j in range(k):
            total_sum[i][j] = sum(files[i:j+1])
    for i in range(k):
        total_sum[i][i] = files[i]

    for i in range(1, k):
        for start in range(k):
            end = start + i
            if end >= k:
                break
            for sep in range(start, end):
                dp[start][end] = min(dp[start][end], dp[start][sep] + dp[sep+1][end] + total_sum[start][end])
    print(dp[0][-1])

