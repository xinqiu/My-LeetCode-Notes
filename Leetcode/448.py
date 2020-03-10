class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # d = {}
        #
        # for num in nums:
        #     d[num] = 1
        #
        # ret = []
        #
        # for num in range(1, len(nums)+1):
        #     if num not in d:
        #         ret.append(num)
        #
        # return ret

        for i in range(len(nums)):
            if nums[abs(nums[i]) - 1] > 0:
                nums[abs(nums[i]) - 1] *= -1

        return [i for i in range(1, len(nums)+1) if nums[i-1] > 0]



solution = Solution()
print solution.findDisappearedNumbers([1, 1, 1])