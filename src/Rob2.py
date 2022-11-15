def rob(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    dp = [0]* (len(nums)-1)
    dp1 = [0] * (len(nums) -1)
    nums1 = nums[0:len(nums)-1]
    nums2 = nums[1:len(nums)]
    if len(nums) == 1:
        return nums[0]
    if len(nums) == 2:
        return max(nums[0], nums[1])
    dp[0] = nums1[0]
    dp[1] = max(nums1[0],nums1[1])
    dp1[0] = nums2[0]
    dp1[1] = max(nums2[0],nums2[1])
    for i in range(2,len(nums1)):
        dp[i] = max(dp[i-1], dp[i-2]+nums1[i])
        dp1[i] = max(dp1[i-1], dp1[i-2]+nums2[i])            

                    
    return max(dp[len(nums)-2], dp1[len(nums)-2])