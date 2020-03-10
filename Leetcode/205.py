class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        d = {}

        if len(set(s)) != len(set(t)):
            return False

        for i in range(len(s)):
            if s[i] not in d:
                d[s[i]] = t[i]
            elif d[s[i]] != t[i]:
                return False
        return True

solution = Solution()

print solution.isIsomorphic('ab', 'aa')