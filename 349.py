def intersection(nums1, nums2):
    if not nums1 or not nums2:
        return []
    dic = {}
    nums = []
    for i in nums1:
        dic[i] = 0
    for j in nums2:
        if j in dic:
            if j not in nums:
                nums.append(j)
    return nums

nums1 = [1,2,2,1]
nums2 = [2,2]
print(intersection(nums1, nums2))