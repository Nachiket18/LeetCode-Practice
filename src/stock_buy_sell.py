class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        min_val = 9999
        max_price = 0
        for i in range(0,len(prices)):
            if prices[i] < min_val:
                min_val = prices[i]
            else:
                tmp = prices[i]
                if (tmp - min_val) > max_price:
                    max_price = (tmp- min_val)
        return max_price
        
