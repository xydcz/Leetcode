def dp(coins, amount):
    m = amount + 1
    dp = [float('inf')] * m
    dp[0] = 0
    for i in range(1, m):
        for j in coins:
            if j <= i:
                dp[i] = min(dp[i], dp[i - j] + 1)
    return -1 if dp[amount] > amount else dp[amount]


coins = [1, 2, 5]
amount = 11
print(dp(coins, amount))
