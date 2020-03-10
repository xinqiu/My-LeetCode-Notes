class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        ret = ''
        maxlen = 0
        for c in s:
            if c not in ret:
                ret += c
            else:
                ret = ret[ret.index(c)+1:]
                ret += c
                # for i in range(len(ret)):
                #     if len(set(ret[i:])) == len(ret[i:]):
                #         ret = ret[i:]
                #         break
            if len(ret) >= maxlen:
                maxlen = len(ret)
        return maxlen

    def lengthOfLongestSubstring1(self, s):
        l = []
        ret = []
        for c in s:
            if c not in l:
                l.append(c)
            else:
                ret.append(len(l))
                l = l[l.index(c)+1:]
                l.append(c)
            ret.append(len(l))
        return max(ret) if ret else 0



solution = Solution()

print(solution.lengthOfLongestSubstring('dcdd'))