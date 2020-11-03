def maxSubArray(nums):
    dp = nums[0]
    s = nums[0]
    for i in range(1, len(nums)):
        s = max(s, dp)
        if dp >= 0:
            dp += nums[i]
        else:
            dp = nums[i]
    return s




nums = [1, -1, 1]
print(maxSubArray(nums))

