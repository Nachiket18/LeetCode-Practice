def deleteAndEarn(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    nums.sort()
    s = set(nums)
    dic = {}
    for i in s:
        dic[i] = nums.count(i)

    uniq = list(s)
    if len(uniq) == 1:
        return uniq[0] * dic[uniq[0]]

    prev1 = uniq[0] * dic[uniq[0]]

    if uniq[1]-1 in uniq:
        prev2 = max(prev1, uniq[1] * dic[uniq[1]])
    else:
        prev2 = prev1 + (uniq[1] * dic[uniq[1]])

    for i in range(2,len(uniq)):
        if uniq[i]-1 in uniq:
            temp = max(prev1 + (uniq[i] * dic[uniq[i]]), prev2)
        else:
            temp = prev2 + (uniq[i] * dic[uniq[i]])
        prev1 = prev2
        prev2 = temp

    return max(prev1, prev2)