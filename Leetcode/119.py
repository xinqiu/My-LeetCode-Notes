class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        rowIndex = rowIndex + 1
        ret = [[1 for i in range(1, rowIndex + 1) if i <= j] for j in range(1, rowIndex + 1)]

        for i in range(2, rowIndex):
            for j in range(1, i):
                ret[i][j] = ret[i - 1][j - 1] + ret[i - 1][j]

        return ret[-1]

class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        if rowIndex == 0:
            return [1]
        rowIndex += 1
        ret = [1]
        while len(ret) < rowIndex:
            ret = [a+b for a, b in zip([0]+ret, ret+[0])]
        return ret

solution = Solution()

print solution.getRow(0)