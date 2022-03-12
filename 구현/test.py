def solution(money, costs):
    answer = 0

    coins = [1,5, 10, 50, 100, 500]
    tree = {0:0}
    for i in range(6):
        tree[coins[i]] = costs[i]
    dp = [0] * (money + 1)
    dp[1] = tree[1]
    for i in range(2, money + 1):
        dp[i] = dp[i-1] + tree[1]
        if i >= 5 and i % 5 == 0:
            dp[i] = min(dp[i], dp[i - 5] + tree[5])
        
        if i >= 10 and i % 10 == 0:
            dp[i] = min(dp[i], dp[i - 10] + tree[10])
        
        if i >= 50 and i % 50 == 0:
            dp[i] = min(dp[i], dp[i - 50] + tree[50])
        
        if i >= 100 and i % 100 == 0:
            dp[i] = min(dp[i], dp[i - 100] + tree[100])
        
        if i >= 500 and i % 500 == 0:
            dp[i] = min(dp[i], dp[i - 500] + tree[500])

    return dp[-1]