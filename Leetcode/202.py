class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """

        while n != 1:
            n = sum([int(c) ** 2 for c in str(n)])
            if n == 4:
                return False
        return True

solution = Solution()

print solution.isHappy(19)