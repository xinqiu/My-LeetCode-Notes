class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        import math
        return int(math.sqrt(x))

solution = Solution()

print solution.mySqrt(4)