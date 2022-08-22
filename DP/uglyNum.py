# 못생긴 수
# DP로 풀어보기
n = int(input())

dp = [0] * n
dp[0] = 1
idx_2 = 0
idx_3 = 0
idx_5 = 0
nxt2 = 2
nxt3 = 3
nxt5 = 5
result = 1
for i in range(1, n):
    
    dp[i] = min(nxt2, nxt3, nxt5)

    if nxt2 == dp[i]:
        idx_2 += 1
        nxt2 = dp[idx_2] * 2
    if nxt3 == dp[i]:
        idx_3 += 1
        nxt3 = dp[idx_3] * 3
    if nxt5 == dp[i]:
        idx_5 += 1
        nxt5 = dp[idx_5] * 5
    
print(dp)