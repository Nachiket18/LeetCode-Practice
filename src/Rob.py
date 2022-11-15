def rob(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = [0]* (len(nums))
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])
        dp[0] = nums[0]
        dp[1] = max(nums[0],nums[1])
        for i in range(2,len(nums)):
            if i == len(nums)-1:
                if dp[0]!= nums[i]:
                    dp[i] = max(dp[i-1], dp[i-2]+nums[i])
                    break
                else:
                    dp[i] = dp[i-1]
                    break
            dp[i] = max(dp[i-1], dp[i-2]+nums[i])

                     
        return dp[len(nums)-1]



