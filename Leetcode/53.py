class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ret = nums[0]
        t = 0
        for n in nums:
            if t > 0:
                t += n
            else:
                t = n
            ret = max(t, ret)
        return ret


solution = Solution()

print solution.maxSubArray([-2,1,-3,4,-1,2,1,-5,4])