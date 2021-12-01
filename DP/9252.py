# LCS 2
str1 = input()
str2 = input()
dp = [[''] * (len(str2) + 1) for _ in range(len(str1) + 1)]

for i in range(len(str1)):
    n = i + 1
    for j in range(len(str2)):
        m = j + 1
        if str1[i] == str2[j]:
            dp[n][m] = dp[i][j] + str1[i]
        else:
            if len(dp[n][m-1]) > len(dp[n-1][m]):
                dp[n][m] = dp[n][m-1]
            else:
                dp[n][m] = dp[n-1][m]

result = len(dp[-1][-1])
print(result)
if result != 0:
    print(dp[-1][-1])
