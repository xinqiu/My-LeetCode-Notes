class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # return 1 if nums == [0] else len(nums) * (len(nums)+1) / 2  - sum(nums)
        return reduce(lambda x, y: x ^ y, map(lambda x: x[0] ^ x[1], list(enumerate(nums)))) ^ len(nums)

solution = Solution()

print solution.missingNumber([9,6,4,2,3,5,7,0,1])