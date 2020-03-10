class Solution(object):
    def toHex(self, num):
        """
        :type num: int
        :rtype: str
        """
        num = num & 0xFFFFFFFF

        ret = ""

        s = "0123456789abcdef"

        while num > 0:
            ret += s[num & 0xf]
            num >>= 4

        return ret[::-1] if ret else "0"



solution = Solution()

print solution.toHex(26)