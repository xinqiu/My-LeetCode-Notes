class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        low, high = 1, n

        while low <= high:
            mid = low + (high-low) // 2
            if guess(mid) == 0:
                return mid
            elif guess(mid) == -1:
                high = mid - 1
            else:
                low = mid + 1