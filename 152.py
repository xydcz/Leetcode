def multiply(nums):
    dp = [[0]*(len(nums)+1) for _ in range(2)]
    dp[1][0] = dp[0][0] = res = nums[0]
    for i in range(1, len(nums)):
        # a = dp[0][i-1]*nums[i]
        # b = dp[1][i-1]*nums[i]
        # dp[0][i] = max(a, b)
        # dp[1][i] = min(a, b)
        dp[0][i] = max(dp[0][i-1]*nums[i], dp[1][i-1]*nums[i], nums[i])
        dp[1][i] = min(dp[0][i-1]*nums[i], dp[1][i-1]*nums[i], nums[i])
        res = max(res, dp[0][i])
    return res


nums = [-1, -2, -9, -6]
print(multiply(nums))


