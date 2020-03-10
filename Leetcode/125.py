class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        t = [c for c in s.lower() if c.isalpha()]
        return t == t[::-1]

solution = Solution()

print solution.isPalindrome("OP")