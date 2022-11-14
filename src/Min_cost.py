def minCostClimbingStairs(self, cost):
    """
    :type cost: List[int]
    :rtype: int
    """
    prev2 = cost[0]
    prev1 = cost[1]
    for i in range(2,len(cost)):
        temp = min(cost[i]+ prev2,cost[i] + prev1)
        prev2 = prev1
        prev1 = temp
        
        
    
    return min(prev1, prev2)