class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        from collections import Counter

        return len(Counter(ransomNote) - Counter(magazine)) == 0


solution = Solution()

print solution.canConstruct("aa", "ab")