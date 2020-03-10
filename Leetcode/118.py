# class Solution(object):
#     def generate(self, numRows):
#         """
#         :type numRows: int
#         :rtype: List[List[int]]
#         """
#
#         ret = [[1 for i in range(1, numRows+1) if i <= j] for j in range(1, numRows+1)]
#
#         for i in range(2, numRows):
#             for j in range(1, i):
#                 ret[i][j] = ret[i-1][j-1]+ret[i-1][j]
#
#         return ret

class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """

        if numRows == 0:
            return []
        ret = [[1]]
        while len(ret) < numRows:
            ret.append([a+b for a, b in zip([0]+ret[-1], ret[-1]+[0])])
        return ret


solution = Solution()

print solution.generate(0)