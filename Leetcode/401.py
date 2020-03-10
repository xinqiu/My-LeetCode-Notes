class Solution(object):
    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        return ["%d:%02d" % (h, m) for h in range(12) for m in range(60) if bin(h).count('1')+bin(m).count('1') == num]

solution = Solution()

print solution.readBinaryWatch(1)

print 