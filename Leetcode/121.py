# class Solution(object):
#     def maxProfit(self, prices):
#         """
#         :type prices: List[int]
#         :rtype: int
#         """
#         ret = 0
#
#         if len(prices) <= 1:
#             return 0
#
#         p = 0
#         for i in range(1, len(prices)):
#             if prices[i] - prices[p] >= ret:
#                 ret = prices[i] - prices[p]
#             elif prices[i] < prices[p]:
#                 p = i
#             else:
#                 pass
#
#         return ret

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        min_p, max_p = 1e9, 0
        for p in prices:
            min_p = min(min_p, p)
            max_p = max(max_p, p-min_p)
        return max_p


solution = Solution()

print solution.maxProfit([7,1,5,3,6,4])