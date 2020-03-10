class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        return [int(c) for c in str(int(''.join(map(str, digits)))+1)]


solution = Solution()

print solution.plusOne([9])