class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """

        for c in s:
            if s.index(c) == len(s) - 1 - s[::-1].index(c):
                return s.index(c)
        return -1


solution = Solution()

print solution.firstUniqChar("loveleetcode")
