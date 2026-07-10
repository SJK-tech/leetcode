class Solution(object):
    def maxProfit(self, prices):
        min=prices[0]
        maxp= 0
        for p in prices:
            if p<min:
                min=p
            profit=p-min

            if profit>maxp:
                maxp=profit
        return maxp
        """
        :type prices: List[int]
        :rtype: int
        """
        