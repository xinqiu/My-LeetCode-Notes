# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

def isBadVersion(version):
    if version >= 4:
        return True
    else:
        return False


class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        low, high = 1, n
        while low < high:
            mid = low + (high - low) / 2
            if isBadVersion(mid):
                high = mid
            else:
                low = mid + 1

        return high

solution = Solution()

print solution.firstBadVersion(5)