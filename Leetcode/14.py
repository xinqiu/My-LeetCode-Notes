class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if strs == []:
            return ""
        strs = sorted(strs)
        str1 = strs[0]
        str2 = strs[-1]
        ret = 0
        for i in range(min(len(str1), len(str2))):
            if str1[i] == str2[i]:
                ret += 1
            else:
                break

        return str1[:ret]


solution = Solution()
print(solution.longestCommonPrefix(['a', 'b']))

