class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if target not in nums:
            nums.append(target)
            nums = sorted(nums)

        return nums.index(target)


solution = Solution()

print solution.searchInsert([1,3,5,6], 0)