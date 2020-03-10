class Solution(object):
    def findContinuousSequence(self, target):
        """
        :type target: int
        :rtype: List[List[int]]
        """

        # nums = list(range(1, target))
        # d = {}
        # ret = []
        # for i in range(target):
        #     if i*(i+1)/2 - target in d:
        #         ret.append(nums[d[i*(i+1)/2-target]: i])
        #     d[i*(i+1)/2] = i
        #
        # return ret

        s = [(1 + i) * i / 2 for i in range(target)]
        nums = list(range(1, target))
        d = {}
        ret = []
        for i, v in enumerate(s):
            if v - target in d:
                ret.append(nums[d[v - target]: i])
            d[v] = i

        return ret

solution = Solution()

print solution.findContinuousSequence(9)