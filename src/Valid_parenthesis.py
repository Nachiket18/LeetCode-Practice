class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        dict = {')':'(', '}':'{', ']':'['}
        a = []
        for i in s:
            if len(a)==0 or not i in dict.keys():
                a.append(i)
            elif dict.get(i)==a[-1]:
                del a[-1]
            else:
                a.append(i)
        return len(a)==0
            