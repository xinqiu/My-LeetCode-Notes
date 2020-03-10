class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num < 1:
            return False

        while num % 5 == 0:
            num /= 5

        while num % 3 == 0:
            num /= 3

        while num % 2 == 0:
            num >>= 1
        return num == 1



solution = Solution()

print solution.isUgly(10)