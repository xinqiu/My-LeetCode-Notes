class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n <= 0:
            return ""
        ret = ""
        while n > 0:
            n -= 1
            t = n % 26
            ret += str(chr(t+ord('A')))
            n /= 26
        return ret[::-1]

solution = Solution()

print solution.convertToTitle(701)