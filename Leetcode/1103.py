class Solution(object):
    def distributeCandies(self, candies, num_people):
        """
        :type candies: int
        :type num_people: int
        :rtype: List[int]
        """

        ret = [0 for _ in range(num_people)]

        cnt = 0

        while candies != 0:

            ret[cnt % num_people] += min(cnt + 1, candies)
            candies -= min(cnt+1, candies)
            cnt += 1

        return ret

solution = Solution()

print solution.distributeCandies(10, 3)
