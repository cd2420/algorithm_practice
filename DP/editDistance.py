# 편집거리
a, b = input(), input()
dp = [[0] * (len(a) + 1) for _ in range(len(b)+1)]
for i in range(1, len(b)+1):
    word_b = b[i-1]
    for j in range(1, len(a)+1):
        word_a = a[j-1]
        if word_a == word_b:
            dp[i][j] = max(dp[i][j], dp[i-1][j-1] + 1)
        else :
            dp[i][j] = max(dp[i][j-1], dp[i-1][j] ,dp[i-1][j-1])
result = max(len(a), len(b))
result -= dp[-1][-1]
print(result)