class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

        ret = 0

        for i in range(len(s)):
            if i < len(s) - 1 and d[s[i]] < d[s[i+1]]:
                ret -= d[s[i]]
            else:
                ret += d[s[i]]

        return ret

solution = Solution()

print(solution.romanToInt('MCMXCIV'))