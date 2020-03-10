class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        t = reduce(lambda x, y: x^y, nums)
        return list(set(map(lambda x: t ^ x, nums)) & set(nums))