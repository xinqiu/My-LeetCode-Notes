class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        if ' ' not in s:
            return len(s)
        else:
            return len(s.split()[-1]) if len(s.split()) > 0 else 0

solution = Solution()


print solution.lengthOfLastWord('1 ')