# class Solution(object):
#     def addDigits(self, num):
#         """
#         :type num: int
#         :rtype: int
#         """
#         while len(str(num)) != 1:
#             num = sum(map(int, str(num)))
#         return num

class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        return num if num < 10 else (num-1)%9+1

solution = Solution()

print solution.addDigits(0)