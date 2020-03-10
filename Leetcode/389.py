class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        # from collections import Counter
        #
        # return (Counter(t) - Counter(s)).keys()[0]

        return chr(reduce(lambda x, y: x ^ y, map(ord,s+t)))


solution = Solution()

print solution.findTheDifference("abcd", "abcde")
