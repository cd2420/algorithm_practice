# 암호코드

words = [str(i) for i in range(1, 27)]
password = input()
password = password
n = len(password)
dp = [0] * n
if password[0] not in words:
    print(0)
else:
    dp[0] = 1
    if n >= 2:
        if password[1] in words:
            dp[1] = 1
        if password[:2] in words:
            dp[1] += 1

    is_possible = True
    for i in range(2, n):
        if password[i] in words:
            dp[i] += (dp[i-1] % 1000000)
        if password[i-1:i+1] in words:
            dp[i] += (dp[i-2] % 1000000)
        if dp[i] == 0:
            is_possible = False
            break
    if is_possible:
        print(dp[-1] % 1000000)
    else:
        print(0)
