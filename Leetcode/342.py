class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """

        return bin(num)[2] == "1" and len(bin(num)[3:]) % 2 == 0 \
               and bin(num)[2:].count("1") == 1

solution = Solution()

solution.isPowerOfFour(2)