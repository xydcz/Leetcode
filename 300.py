def lenthOfLTS(nums):
    dp = [1] * len(nums)
    print(dp)
    res = 1
    for i in range(1, len(nums)):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j]+1)
        res = max(dp[i], res)
    print(dp)
    return res


nums = [10, 9, 2, 5, 3, 7, 101, 18]
print(lenthOfLTS(nums))