class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        str = str.split()

        d = {}

        if len(set(pattern)) != len(set(str)) or len(pattern) != len(str):
            return False

        for i in range(len(pattern)):
            if pattern[i] not in d:
                d[pattern[i]] = str[i]
            elif d[pattern[i]] != str[i]:
                return False
        return True

        # return list(map(pattern.index, pattern)) == list(map(str.index, str))


solution = Solution()
print solution.wordPattern("aba", "cat cat cat dog")