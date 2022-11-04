class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        min_val = 10000
        for i in strs:
            if len(i) < min_val:
                min_val  = len(i)

        output = ""
        for i in range(0,min_val):
            character_com = strs[0][i] ## 0. f,  1. l 2. o
            match = 1
            for string in strs:
                #print (string[i])
                if string[i] != character_com:
                    match = 0
                    break
            if match == 1:
                print(character_com)
                output += character_com
            else:
                break

        return output
