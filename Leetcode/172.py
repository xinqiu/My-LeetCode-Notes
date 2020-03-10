class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        ret = 0
        while n >= 5:
            ret += n / 5
            n /= 5
        return ret

solution = Solution()

print solution.trailingZeroes(25)