class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        ret = int(str(x)[::-1]) if x >= 0 else -int(str(x)[1:][::-1])

        if -2**31 <= ret <= 2**31-1:
            return ret
        else:
            return 0


solution = Solution()

print(solution.reverse(123))