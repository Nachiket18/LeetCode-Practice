class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        i_index = m
        
        for i in range(0,len(nums2)):
            match = 0
            for j in range(0,len(nums1)):
                if nums2[i] <= nums1[j]:
                    nums1.insert(j,nums2[i])
                    match = 1
                    i_index += 1
                    break
            if match == 0:
                nums1[i_index] = nums2[i]
                i_index += 1
        
        print(nums1)
        
        
        for k in range((m+n),len(nums1)):
            nums1.pop()
    
        return nums1
