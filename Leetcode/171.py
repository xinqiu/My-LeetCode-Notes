class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        ret = 0
        for c in s:
            ret = (ord(c) - ord('A') + 1) + ret * 26
        return ret


s = 'ZY'

print reduce(lambda x, y: x*26+y,[ord(c)-ord('A')+1 for c in s])