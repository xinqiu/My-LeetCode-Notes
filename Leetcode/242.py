class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        from collections import Counter
        return Counter(s) == Counter(t)

solution = Solution()

print solution.isAnagram('aacc', 'ccac')