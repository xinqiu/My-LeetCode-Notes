class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = list(s)
        i, j = 0, len(s) - 1
        while i < j:
            if s[i] in 'aeiouAEIOU' and s[j] in 'aeiouAEIOU':
                s[i], s[j] = s[j], s[i]
                i += 1
                j -= 1
            elif s[i] not in 'aeiouAEIOU':
                i += 1
            elif s[j] not in 'aeiouAEIOU':
                j -= 1
        return ''.join(s)

solution = Solution()

print solution.reverseVowels("hello")