class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return n > 0 and (n & (n-1)) == 0


solution = Solution()

print solution.isPowerOfTwo(4)