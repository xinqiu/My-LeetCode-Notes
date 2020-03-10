class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        count = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                count += 1
            elif count > 0:
                nums[i-count] = nums[i]
                nums[i] = 0

solution = Solution()

print solution.moveZeroes([0,1,0,3,12])
