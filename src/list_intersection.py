class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        m = len(nums1)
        n = len(nums2)
        
        match_dict = {}
        output_cm = {}
        output_final = []
        
        if m > n:
            for i in range(0,len(nums2)):
                match_dict[nums2[i]] = nums2.count(nums2[i])
                output_cm [nums2[i]] = nums1.count(nums2[i])            
                        
        else:
            for i in range(0,len(nums1)):
                match_dict[nums1[i]] = nums1.count(nums1[i])
                output_cm [nums1[i]] = nums2.count(nums1[i])\
                       
                        
        
        for elem in output_cm:
            tmp = match_dict[elem]
            tmp_2 = output_cm[elem]
            
            min_tmp = min(tmp,tmp_2)
            
            for i in range(min_tmp):
                output_final.append(elem)
            
        return output_final
