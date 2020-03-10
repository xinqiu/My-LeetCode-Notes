class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        d = {}
        for i, n in enumerate(nums):
            if target-n in d:
                return d[target-n], i
            d[n] = i


solution = Solution()

print(solution.twoSum([2,7,11,15], 9))