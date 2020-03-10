class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        # ret = 0
        #
        # for i in range(1, len(prices)):
        #     if prices[i] > prices[i-1]:
        #         ret += prices[i] - prices[i-1]
        # return ret

        return sum(filter(lambda x:x > 0, [prices[i] - prices[i-1] for i in range(1, len(prices))]))

solution = Solution()

print solution.maxProfit([7,1,5,3,6,4])