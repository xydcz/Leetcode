def dp(coins, amount):
    m = amount + 1
    dp = [float('inf')] * m
    dp[0] = 0
    for i in range(1, m):
        for j in range(len(coins)):
            if coins[j] <= i:
                dp[i] = min(dp[i], dp[i - coins[j]] + 1)
    return -1 if dp[amount] > amount else dp[amount]


coins = [1, 2, 5]
# coins = [2]
amount = 11
print(dp(coins, amount))