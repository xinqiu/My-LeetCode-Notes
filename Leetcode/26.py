class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        t = None
        num = nums[:]
        for n in num:
            if n != t:
                t = n
            else:
                nums.remove(n)
        return len(nums)

solution = Solution()

print(solution.removeDuplicates([0,0,1,1,1,2,2,3,3,4]))